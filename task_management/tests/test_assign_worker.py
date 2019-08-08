from django.test import TestCase


class AssignWorkerTest(TestCase):

    def testcase_01(self):
        create_request = {
            "name": "deepak",
            "email": "kapeed2091@gmail.com",
            "company_name": "iB"
        }
        from task_management.models import Worker
        from task_management.models import Order
        from task_management.models import OrderWorker

        create_response = Worker.create(**create_request)

        worker_id = create_response['worker_id']

        create_order_request = {
            "title": "Test title",
            "description": "Test description",
            "deadline": "2018-09-20"
        }

        create_order_response = Order.create(**create_order_request)

        order_id = create_order_response['order_id']

        request = {
            "order_id": order_id,
            "worker_id": worker_id
        }

        Order.assign_worker(**request)

        self.assertEqual(1, OrderWorker.objects.all().count(),
                         'Error in AssignWorkerTest.testcase_01')
