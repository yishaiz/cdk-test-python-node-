import aws_cdk as core
import aws_cdk.assertions as assertions

from py_testing.py_testing_stack import PySimpleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in py_testing/py_testing_stack.py
def test_lambda_props():
    app = core.App()
    stack = PySimpleStack(app, "py-testing")
    template = assertions.Template.from_stack(stack)
    
    template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.11",
    })
    # assert lambda.runtime == aws_cdk.aws_lambda.Runtime.PYTHON_3_11
    


