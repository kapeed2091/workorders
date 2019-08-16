from django.test import TestCase
from sqreen_demo.views import check_signature


class TestCheckSignature(TestCase):
    secret_key = b'sqreen'

    def test_success_1(self):
        request_signature = '17f2b34012b5ab323ed862c0851ac4dbd2ce852f227c7c1f9421846d14f3b0bb'
        request_body = b'[{"sqreen_payload_type": "test", "application_id": "5d5147b6f7728b0023934b3f", "application_name": "\\"workorders\\"", "environment": "development", "id": "13e12174e78aece0a3936532178e8e50", "event_category": "test", "event_kind": "test_kind", "risk": 42, "date_occurred": "2019-08-16T18:56:33.080773+00:00", "humanized_description": "", "url": "http://test", "ips": [{"address": "42.42.42.42", "date_resolved": "2019-08-16T18:56:33.080821+00:00"}]}]'
        status = check_signature(self.secret_key, request_signature,
                                 request_body)
        self.assertEqual(status, True,
                         'Error in TestCheckSignature.test_success_1')

    def test_success_2(self):
        request_signature = 'b1225023ce7f357d95b1a70b9a2957c5662a26cbec82e1eb962376131f95dcdf'
        request_body = b'[{"sqreen_payload_type": "test", "application_id": "5d5147b6f7728b0023934b3f", "application_name": "\\"workorders\\"", "environment": "development", "id": "b1f3cb4edb79e97f88be174ac11a4808", "event_category": "test", "event_kind": "test_kind", "risk": 42, "date_occurred": "2019-08-16T18:58:35.803550+00:00", "humanized_description": "", "url": "http://test", "ips": [{"address": "42.42.42.42", "date_resolved": "2019-08-16T18:58:35.803601+00:00"}]}]'
        status = check_signature(self.secret_key, request_signature,
                                 request_body)
        self.assertEqual(status, True,
                         'Error in TestCheckSignature.test_success_2')

    def test_failure(self):
        request_signature = '17f2b34012b5ab323ed862c0851ac4dbd2ce852f227'
        request_body = b'[{"sqreen_payload_type": "test", "application_id": "5d5147b6f7728b0023934b3f", "application_name": "\\"workorders\\"", "environment": "development", "id": "13e12174e78aece0a3936532178e8e50", "event_category": "test", "event_kind": "test_kind", "risk": 42, "date_occurred": "2019-08-16T18:56:33.080773+00:00", "humanized_description": "", "url": "http://test", "ips": [{"address": "42.42.42.42", "date_resolved": "2019-08-16T18:56:33.080821+00:00"}]}]'
        status = check_signature(self.secret_key, request_signature,
                                 request_body)
        self.assertEqual(status, False,
                         'Error in TestCheckSignature.test_failure')
