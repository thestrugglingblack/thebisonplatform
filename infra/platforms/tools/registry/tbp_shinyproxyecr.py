from aws_cdk import (
    Stack,
    aws_ecr as ecr,
    RemovalPolicy
)
from constructs import Construct

class ShinyProxyECRStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # # # Create TBP Shiny ProxyECR Repository
        self.repository = ecr.Repository(
            self, "TBPProxyRepository",
            repository_name="tbp/tbp-shiny-proxy",
            removal_policy=RemovalPolicy.DESTROY
        )