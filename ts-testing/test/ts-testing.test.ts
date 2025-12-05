import * as cdk from 'aws-cdk-lib';
import * as TsTesting from '../lib/ts-testing-stack';
import { Template, Match } from 'aws-cdk-lib/assertions';
import { PolicyDocument } from 'aws-cdk-lib/aws-iam';

describe('TsSimpleStack test suite', () => {
  let template: Template;

  beforeAll(() => {
    const app = new cdk.App({
      outdir: 'cdk.out/test',
    });
    const stack = new TsTesting.TsSimpleStack(app, 'MyTestStack');
    template = Template.fromStack(stack);
  });

  test('Lambda runtime check', () => {
    template.hasResourceProperties('AWS::Lambda::Function', {
      Runtime: 'nodejs18.x',
    });
    template.resourceCountIs('AWS::Lambda::Function', 1);
  });

  test('Lambda runtime check regex', () => {
    template.hasResourceProperties('AWS::Lambda::Function', {
      Runtime: Match.stringLikeRegexp('nodejs'),
    });
  });

  test('Lambda bucket policy, with matchers', () => {
    template.hasResourceProperties(
      'AWS::IAM::Policy',
      Match.objectLike({
        PolicyDocument: {
          Statement: [{
              Resource: [{
                  'Fn::GetAtt': [
                    Match.stringLikeRegexp('SimpleBucket'),
                    'Arn'
                  ],
                },
                Match.anyValue()
              ],
            }],
        },
      })
    );
  });
});
