from aws_cdk import Stack, RemovalPolicy
from aws_cdk.aws_lambda import Function, LayerVersion, Runtime, Code
from aws_cdk.aws_dynamodb import Table, Attribute, AttributeType
from constructs import Construct


class IdempotencyStack(Stack):
  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    table = Table(self, 'idempotency-table-py',
      table_name='idempotency-py',
      partition_key=Attribute(name='id', type=AttributeType.STRING),
      time_to_live_attribute='expiration',
      removal_policy=RemovalPolicy.DESTROY
    )

    powertools_layer = LayerVersion.from_layer_version_arn(self, 'powertools-layer-py',
      layer_version_arn=f'arn:aws:lambda:us-east-1:017000801446:layer:AWSLambdaPowertoolsPython:29'
    )

    function = Function(self, 'idempotency-lambda-py', 
      runtime=Runtime.PYTHON_3_9,
      layers=[powertools_layer],
      code=Code.from_asset('cdk_playground_py/idempotency'),
      handler='lambda.handler',
      function_name='idempotency-py',
      environment={
        'TABLE_NAME': table.table_name
      }
    )

    table.grant_full_access(function)
