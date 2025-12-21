import jsii
import json
from aws_cdk import IAspect, aws_iam, Stack, Annotations


@jsii.implements(IAspect)
class PolicyChecker:
    def visit(self, node):
        if isinstance(node, aws_iam.CfnPolicy):
            resolvedDoc = Stack.of(node).resolve(node.policy_document)
            resolvedDocJson = json.dumps(resolvedDoc)

            print(resolvedDocJson)

            if 'GetBucket' in resolvedDocJson:
                Annotations.of(node).add_warning_v2(
                    "PolicyChecker:GetBucketNotAllowed",  # id
                    "IAM Policy contains 'GetBucket' action, which is not allowed."
                )

        # print(f"Visiting: {node.__class__.__name__}")
        # print(f"Visiting node: {node}")
