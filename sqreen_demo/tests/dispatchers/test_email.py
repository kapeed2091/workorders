from mock import mock
from django.test import TestCase


def boto3_client(*args, **kwargs):
    return MockSESClient()


class MockSESClient:
    def send_email(self, *args, **kwargs):
        return {'MessageId': '1234'}


@mock.patch('boto3.client', boto3_client)
class TestEmail(TestCase):
    def test_success(self):
        data = 'This is test one'
        from sqreen_demo.dispatchers.email_dispatcher import EmailDispatcher
        dispatcher = EmailDispatcher(data)
        response = dispatcher.notify()
        self.assertEqual(response, None, 'Error in TestEmail.test_one')
