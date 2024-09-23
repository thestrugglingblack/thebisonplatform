#!/usr/bin/env python3
import os

import aws_cdk as cdk
from dotenv import load_dotenv

from platforms.tools.registry.tbp_shinyproxyecr import ShinyProxyECRStack

from platforms.directory.auth.tbp_cognito import ShinyProxyCognitoStack

load_dotenv('../.env')
account_id = os.getenv('AWS_ID')

app = cdk.App()

ShinyProxyECRStack(
    app,
    "TBPShinyProxyECR",
    env=cdk.Environment(
        account=account_id,
        region='us-east-1'
    )
)

ShinyProxyCognitoStack(
    app,
    'TBPShinyProxyCognito',
    env=cdk.Environment(
        account=account_id,
        region='us-east-1'
    )
)

app.synth()
