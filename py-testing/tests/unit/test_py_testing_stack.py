import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest


from aws_cdk.assertions import Match, Capture

from py_testing.py_testing_stack import PySimpleStack


@pytest.fixture(scope='session')
def simple_template():
    print("Setting up the test fixture")
    app = core.App()
    stack = PySimpleStack(app, "py-testing")
    template = assertions.Template.from_stack(stack)
    return template


def test_lambda_props(simple_template):
    simple_template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": "python3.11",
    })

    simple_template.resource_count_is("AWS::Lambda::Function", 1)


def test_lambda_runtime_with_matcher(simple_template):
    simple_template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": Match.string_like_regexp("python*"),
    })


def test_lambda_runtime_with_matcher2(simple_template):
    simple_template.has_resource_properties("AWS::Lambda::Function", {
        "Runtime": Match.string_like_regexp("python3.*"),
    })

    # simple_template.resource_count_is("AWS::Lambda::Function", 1)


def test_lambda_bucket_with_matchers(simple_template):
    simple_template.has_resource_properties(
        "AWS::IAM::Policy",
        Match.object_like(
            {
                "PolicyDocument": {
                    "Statement": [
                        {
                            "Resource": [
                                {
                                    "Fn::GetAtt": [
                                        Match.string_like_regexp(
                                            "SimpleBucket"),
                                        "Arn",
                                    ]
                                },
                                Match.any_value()
                            ]
                        }
                    ]
                }
            }
        ),
    )


def test_lambda_actions_with_captures(simple_template):
    lambda_action_capture = Capture()

    simple_template.has_resource_properties(
        "AWS::IAM::Policy",
        {
            "PolicyDocument": {
                "Statement": [
                    {
                        "Action": lambda_action_capture,
                    }
                ]
            }
        }
    )

    expected_actions = [
        "s3:GetBucket*",
        "s3:GetObject*",
        "s3:List*"
    ]

    assert sorted(lambda_action_capture.as_array()) == sorted(expected_actions)

    assert set(lambda_action_capture.as_array()) == set(expected_actions)

    assert "s3:GetObject*" in expected_actions


# add a snapshot test to capture the bucket template
def test_bucket_props_with_snapshot(simple_template, snapshot):
    bucket_template = simple_template.find_resources("AWS::S3::Bucket")
    
    assert bucket_template == snapshot

    # # Use snapshot testing to capture the bucket template
    # snapshot = assertions.Match.object_like(bucket_template)

    # # Here we would normally compare with a stored snapshot
    # # For demonstration, we will just print it out
    # print(snapshot)
