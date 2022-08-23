import os
from aws_cdk import App, Environment
from cdk_playground_py.idempotency import IdempotencyStack

# for development, use account/region from cdk cli
dev_env = Environment(
  account=os.getenv('CDK_DEFAULT_ACCOUNT'),
  region=os.getenv('CDK_DEFAULT_REGION')
)

app = App()
IdempotencyStack(app, "idempotency-py", env=dev_env)

app.synth()