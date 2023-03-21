# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessRuleDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Direction that specifies whether the access rules is inbound/outbound."""

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class AddressPrefixType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Address prefix type."""

    IP_PREFIX = "IPPrefix"
    SERVICE_TAG = "ServiceTag"


class AdminRuleKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the rule is custom or default."""

    CUSTOM = "Custom"
    DEFAULT = "Default"


class AssociationAccessMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Access mode on the association."""

    LEARNING = "Learning"
    ENFORCED = "Enforced"
    AUDIT = "Audit"


class ConfigurationType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Configuration Deployment Type."""

    SECURITY_ADMIN = "SecurityAdmin"
    SECURITY_USER = "SecurityUser"
    CONNECTIVITY = "Connectivity"


class ConnectivityTopology(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Connectivity topology type."""

    HUB_AND_SPOKE = "HubAndSpoke"
    MESH = "Mesh"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class DeleteExistingNSGs(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Flag if need to delete existing network security groups."""

    FALSE = "False"
    TRUE = "True"


class DeleteExistingPeering(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Flag if need to remove current existing peerings."""

    FALSE = "False"
    TRUE = "True"


class DeploymentStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Deployment Status."""

    NOT_STARTED = "NotStarted"
    DEPLOYING = "Deploying"
    DEPLOYED = "Deployed"
    FAILED = "Failed"


class EffectiveAdminRuleKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the rule is custom or default."""

    CUSTOM = "Custom"
    DEFAULT = "Default"


class EffectiveUserRuleKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the rule is custom or default."""

    CUSTOM = "Custom"
    DEFAULT = "Default"


class GroupConnectivity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Group connectivity type."""

    NONE = "None"
    DIRECTLY_CONNECTED = "DirectlyConnected"


class IsGlobal(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Flag if global mesh is supported."""

    FALSE = "False"
    TRUE = "True"


class MembershipType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Membership Type."""

    STATIC = "Static"
    DYNAMIC = "Dynamic"


class NspLinkProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state of NSP Link/LinkReference."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    ACCEPTED = "Accepted"
    FAILED = "Failed"
    WAIT_FOR_REMOTE_COMPLETION = "WaitForRemoteCompletion"


class NspLinkStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The NSP link state."""

    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class NspProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    ACCEPTED = "Accepted"
    FAILED = "Failed"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current provisioning state."""

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"


class SecurityConfigurationRuleAccess(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether network traffic is allowed or denied."""

    ALLOW = "Allow"
    DENY = "Deny"
    ALWAYS_ALLOW = "AlwaysAllow"


class SecurityConfigurationRuleDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of the rule. The direction specifies if the rule will be evaluated on incoming or
    outgoing traffic.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class SecurityConfigurationRuleProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Network protocol this rule applies to."""

    TCP = "Tcp"
    UDP = "Udp"
    ICMP = "Icmp"
    ESP = "Esp"
    ANY = "Any"
    AH = "Ah"


class SecurityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Security Type."""

    ADMIN_POLICY = "AdminPolicy"
    USER_POLICY = "UserPolicy"


class UseHubGateway(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Flag if need to use hub gateway."""

    FALSE = "False"
    TRUE = "True"


class UserRuleKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether the rule is custom or default."""

    CUSTOM = "Custom"
    DEFAULT = "Default"