#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_ecr_resource_policy.cdk_ecr_resource_policy_stack import (
    CdkEcrResourcePolicyStack,
)

app = cdk.App()
CdkEcrResourcePolicyStack(app, "cdk-ecr-resource-policy")

app.synth()
