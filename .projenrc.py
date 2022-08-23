from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
  author_email="marciocadev@gmail.com",
  author_name="Marcio Almeida",
  cdk_version="2.38.1",
  module_name="cdk_playground_py",
  name="cdk-playground-py",
  version="0.1.0",

  deps=[
    'aws-lambda-powertools@1.27.0'
  ]
)

project.synth()