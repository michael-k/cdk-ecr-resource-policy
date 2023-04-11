from aws_cdk import Stack, aws_ecr as ecr, aws_iam as iam
from constructs import Construct


class CdkEcrResourcePolicyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        repository = ecr.Repository(
            self,
            "Repository",
        )

        repository.add_to_resource_policy(
            iam.PolicyStatement(
                sid="AllowPullFromOtherAccounts",
                actions=[
                    "ecr:BatchCheckLayerAvailability",
                    "ecr:BatchGetImage",
                    "ecr:GetDownloadUrlForLayer",
                ],
                principals=[
                    iam.AccountPrincipal("111122223333"),
                    iam.AccountPrincipal("123456789012"),
                ],
                effect=iam.Effect.ALLOW,
            )
        )
