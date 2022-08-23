import os
from aws_lambda_powertools.utilities.idempotency import (
  DynamoDBPersistenceLayer, idempotent
)

persistence_layer = DynamoDBPersistenceLayer(table_name=os.environ.get('TABLE_NAME'))

@idempotent(persistence_store=persistence_layer)
def handler(event, context):
  print(event)
  return {
    "id": event['id'],
    "statusCode": 200,
    "body": "ok"
  }