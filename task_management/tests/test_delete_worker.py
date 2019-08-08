from django.test import TestCase


class DeleteWorkerTest(TestCase):

    def testcase_01(self):
        create_request = {
            "name": "deepak",
            "email": "kapeed2091@gmail.com",
            "company_name": "iB"
        }
        from task_management.models import Worker
        create_response = Worker.create(**create_request)

        worker_id = create_response['worker_id']

        self.assertEqual(1, Worker.objects.all().count(),
                         'Error in DeleteWorkerTest.testcase_01')

        Worker.remove(worker_id)

        self.assertEqual(0, Worker.objects.all().count(),
                         'Error in DeleteWorkerTest.testcase_01')
