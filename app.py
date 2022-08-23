import os
from aws_cdk import App, Environment
from cdk_playground_py.main import MyStack

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('CDK_DEFAULT_REGION')
)

app = App()
MyStack(app, "cdk-playground-py-dev", env=dev_env)
# MyStack(app, "cdk-playground-py-prod", env=prod_env)

app.synth()