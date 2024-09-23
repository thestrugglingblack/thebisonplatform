import os
from aws_cdk import (
    Stack,
    aws_cognito as cognito
)

from constructs import Construct


class ShinyProxyCognitoStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        user_pool = cognito.UserPool(
            self,
            "TBPUserPool",
            user_pool_name="TBPUserPool",
            self_sign_up_enabled=True,
            auto_verify=cognito.AutoVerifiedAttrs(email=True),
            sign_in_aliases=cognito.SignInAliases(email=True),
            password_policy=cognito.PasswordPolicy(
                min_length=12,
                require_digits=True,
                require_symbols=True,
                require_lowercase=True,
                require_uppercase=True
            ),
            advanced_security_mode=cognito.AdvancedSecurityMode.ENFORCED
        )

        callback_urls = ["https://localhost:8080/login/oauth2/code/"]  # Update with your domain
        logout_urls = ["https://localhost:8080/logout"]  # Update with your logout URL

        tbp_app_client = cognito.UserPoolClient(
            self, "TBPAppClient",
            user_pool=user_pool,
            generate_secret=True,
            auth_flows=cognito.AuthFlow(
                user_password=True,
                user_srp=True
            ),
            o_auth=cognito.OAuthSettings(
                flows=cognito.OAuthFlows(
                    implicit_code_grant=True,  # Enable implicit grant
                ),
                scopes=[  # Required scopes for ShinyProxy
                    cognito.OAuthScope.OPENID,
                    cognito.OAuthScope.EMAIL,
                    cognito.OAuthScope.PROFILE
                ],
                callback_urls=callback_urls,  # Where Cognito should redirect after successful login
                logout_urls=logout_urls  # Where Cognito should redirect after logout
            )
        )

        user_pool.add_domain(
            'TBPDomain',
            cognito_domain=cognito.CognitoDomainOptions(domain_prefix='thebisonplatform')
        )

        identity_pool = cognito.CfnIdentityPool(
            self,
            'TBPIdentityPool',
            allow_unauthenticated_identities=False,
            cognito_identity_providers=[
                cognito.CfnIdentityPool.CognitoIdentityProviderProperty(
                    client_id=tbp_app_client.user_pool_client_id,
                    provider_name=user_pool.user_pool_provider_name
                )
            ]
        )
