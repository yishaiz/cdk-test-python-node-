import * as cdk from 'aws-cdk-lib';
import * as TsTesting from '../lib/ts-testing-stack';
import { Template } from 'aws-cdk-lib/assertions';

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

  // test('Lambda runtime check', () => {
  //   template.hasResourceProperties('AWS::Lambda::Function', {
  //     Runtime: 'nodejs18.x',
  //   });
  // });
});

// code: Code.fromInline('console.log()'),
//  "ZipFile": "console.log()"
// },
// "Handler": "index.handler",
