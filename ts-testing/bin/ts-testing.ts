#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { TsSimpleStack } from '../lib/ts-testing-stack';

const app = new cdk.App();
new TsSimpleStack(app, 'TsTestingStack', {
  
});
