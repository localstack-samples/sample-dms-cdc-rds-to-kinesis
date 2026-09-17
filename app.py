import os
import aws_cdk as cdk

from dms_sample.stack import DmsSampleStack

STACK_NAME = os.getenv("STACK_NAME", "DMsSampleSetupStack")

app = cdk.App()
dms_sample_stack = DmsSampleStack(app, STACK_NAME)
cdk.Tags.of(dms_sample_stack).add("aws-apn-id", "pc:9yq38ki5jw5mas7jhjthpgveo")

app.synth()
