# Reference: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html


def send_email(body):
    import boto3
    from botocore.exceptions import ClientError
    from sqreen_demo.config import (
        AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,
        SENDER_EMAIL_ID, RECIPIENT_EMAIL_ID, SUBJECT
    )

    AWS_REGION = "eu-west-1"

    BODY_TEXT = body

    CHARSET = "UTF-8"

    client = boto3.client(
        'ses',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )

    MESSAGE_BODY = {
        'Text': {
            'Charset': CHARSET,
            'Data': BODY_TEXT,
        },
    }

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT_EMAIL_ID,
                ],
            },
            Message={
                'Body': MESSAGE_BODY,
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER_EMAIL_ID,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
