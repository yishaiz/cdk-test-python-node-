#!/usr/bin/env python3
import os

import aws_cdk as cdk

from py_testing.py_testing_stack import PyTestingStack


app = cdk.App()
PyTestingStack(app, "PyTestingStack",

               )

app.synth()
