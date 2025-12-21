import jsii
from aws_cdk import IAspect


@jsii.implements(IAspect)
class PolicyChecker:
    def visit(self, node):
        print(f"Visiting node: {node}")
        print(f"Visiting: {node.__class__.__name__}")
