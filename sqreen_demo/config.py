import os
from enum import Enum
from sqreen_demo.dispatchers import *

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

SQREEN_SECRET_KEY = b'sqreen'


class DispatcherEnum(Enum):
    http = {'notify': True, 'class': HTTPDispatcher}
    sms = {'notify': True, 'class': SMSDispatcher}
    email = {'notify': True, 'class': EmailDispatcher}
    slack = {'notify': True, 'class': SlackDispatcher}
    log = {'notify': True, 'class': LogDispatcher}

    @classmethod
    def get_dispatchers_to_notify(cls):
        return [item.value['class'] for item in cls if item.value['notify']]


SENDER_EMAIL_ID = 'kapeed2091@gmail.com'
RECIPIENT_EMAIL_ID = 'kapeed2091@gmail.com'
SUBJECT = 'Received notification from Sqreen'

SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'
