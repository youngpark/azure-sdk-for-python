# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from io import BytesIO

import pytest
from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient, ExponentialRetry

from devtools_testutils import ResponseCallback
from devtools_testutils.storage import StorageRecordedTestCase
from settings.testcase import BlobPreparer
from test_helpers import NonSeekableStream

# test constants
PUT_BLOCK_SIZE = 4 * 1024


class TestStorageBlobRetry(StorageRecordedTestCase):
    # --Helpers-----------------------------------------------------------------
    def _setup(self, bsc):
        self.container_name = self.get_resource_name('utcontainer')
        if self.is_live:
            try:
                bsc.create_container(self.container_name)
            except ResourceExistsError:
                pass

    @pytest.mark.live_test_only
    @BlobPreparer()
    def test_retry_put_block_with_seekable_stream(self, **kwargs):
        storage_account_name = kwargs.pop("storage_account_name")
        storage_account_key = kwargs.pop("storage_account_key")

        # Arrange
        retry = ExponentialRetry(initial_backoff=1, increment_base=2, retry_total=3)
        bsc = BlobServiceClient(
            self.account_url(storage_account_name, "blob"),
            credential=storage_account_key,
            retry_policy=retry
        )

        self._setup(bsc)
        blob_name = self.get_resource_name('blob')
        data = self.get_random_bytes(PUT_BLOCK_SIZE)
        data_stream = BytesIO(data)

        # rig the response so that it fails for a single time
        responder = ResponseCallback(status=201, new_status=408)

        # Act
        blob = bsc.get_blob_client(self.container_name, blob_name)
        blob.stage_block(1, data_stream, raw_response_hook=responder.override_first_status)

        # Assert
        _, uncommitted_blocks = blob.get_block_list(
            block_list_type="uncommitted",
            raw_response_hook=responder.override_first_status)
        assert len(uncommitted_blocks) == 1
        assert uncommitted_blocks[0].size == PUT_BLOCK_SIZE

        # Commit block and verify content
        blob.commit_block_list(['1'], raw_response_hook=responder.override_first_status)

        # Assert
        content = blob.download_blob().readall()
        assert content == data

    @pytest.mark.live_test_only
    @BlobPreparer()
    def test_retry_put_block_with_non_seekable_stream(self, **kwargs):
        storage_account_name = kwargs.pop("storage_account_name")
        storage_account_key = kwargs.pop("storage_account_key")

        # Arrange
        retry = ExponentialRetry(initial_backoff=1, increment_base=2, retry_total=3)
        bsc = BlobServiceClient(
            self.account_url(storage_account_name, "blob"),
            credential=storage_account_key,
            retry_policy=retry
        )

        self._setup(bsc)
        blob_name = self.get_resource_name('blob')
        data = self.get_random_bytes(PUT_BLOCK_SIZE)
        data_stream = NonSeekableStream(BytesIO(data))

        # rig the response so that it fails for a single time
        responder = ResponseCallback(status=201, new_status=408)

        # Act
        blob = bsc.get_blob_client(self.container_name, blob_name)
        # Note: put_block transforms non-seekable streams into byte arrays before handing it off to the executor
        blob.stage_block(1, data_stream, raw_response_hook=responder.override_first_status)

        # Assert
        _, uncommitted_blocks = blob.get_block_list(
            block_list_type="uncommitted",
            raw_response_hook=responder.override_first_status)
        assert len(uncommitted_blocks) == 1
        assert uncommitted_blocks[0].size == PUT_BLOCK_SIZE

        # Commit block and verify content
        blob.commit_block_list(['1'], raw_response_hook=responder.override_first_status)

        # Assert
        content = blob.download_blob().readall()
        assert content == data
