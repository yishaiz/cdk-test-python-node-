import aws_cdk as core
import aws_cdk.assertions as assertions

from py_testing.py_testing_stack import PyTestingStack

# example tests. To run these tests, uncomment this file along with the example
# resource in py_testing/py_testing_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PyTestingStack(app, "py-testing")
    template = assertions.Template.from_stack(stack)


