from django.test import TestCase


class CreateWorkerTest(TestCase):

    def testcase_01(self):
        request = {
            "name": "deepak",
            "email": "kapeed2091@gmail.com",
            "company_name": "iB"
        }
        expected_response = {"worker_id": 1}

        from task_management.models import Worker
        actual_response = Worker.create(**request)

        self.assertEqual(actual_response, expected_response,
                         'Error in CreateWorkerTest.testcase_01')
