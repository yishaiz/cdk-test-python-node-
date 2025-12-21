#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { TsSimpleStack } from '../lib/ts-testing-stack';

const app = new cdk.App();
const tsSimpleStack = new TsSimpleStack(app, 'TsTestingStack');

cdk.Tags.of(tsSimpleStack).add('stage', 'test');

cdk.Tags.of(tsSimpleStack).add('stage', 'main', {
  includeResourceTypes: ['AWS::S3::Bucket'],
});

cdk.Tags.of(tsSimpleStack).add('stage', 'aux', {
  includeResourceTypes: ['AWS::S3::Bucket'],
  priority: 150,
});
