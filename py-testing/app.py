#!/usr/bin/env python3
import os

import aws_cdk as cdk

from py_testing.py_testing_stack import PySimpleStack


app = cdk.App()
my_stack = PySimpleStack(app, "PySimpleStack")

cdk.Tags.of(my_stack).add("stage", "testing")

cdk.Tags.of(my_stack).add("storage", "main",
                          include_resource_types=["AWS::S3::Bucket"],
                          priority=200)

cdk.Tags.of(my_stack).add("storage", "aux",
                          include_resource_types=["AWS::S3::Bucket"])


app.synth()
