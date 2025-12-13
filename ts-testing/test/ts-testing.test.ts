import * as cdk from 'aws-cdk-lib';
import * as TsTesting from '../lib/ts-testing-stack';
import { Template, Match, Capture } from 'aws-cdk-lib/assertions';
import { PolicyDocument } from 'aws-cdk-lib/aws-iam';
// import { PolicyDocument } from 'aws-cdk-lib/aws-iam';

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
          Statement: [
            {
              Resource: [
                {
                  'Fn::GetAtt': [Match.stringLikeRegexp('SimpleBucket'), 'Arn'],
                },
                Match.anyValue(),
              ],
            },
          ],
        },
      })
    );
  });

  test('Lambda actions with capture', () => {
    const lambdaActionsCapture = new Capture();

    template.hasResourceProperties('AWS::IAM::Policy', {
      PolicyDocument: {
        Statement: [
          {
            Action: lambdaActionsCapture,
          },
        ],
      },
    });
  });
});

//     template.hasResourceProperties('AWS::Lambda::Function', {
//   Runtime: Match.stringLikeRegexp('nodejs'),
// });
