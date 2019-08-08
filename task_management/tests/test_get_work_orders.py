from django.test import TestCase


class GetWorkOrdersTest(TestCase):

    def testcase_01(self):
        import datetime
        from task_management.models import Worker
        from task_management.models import Order
        from task_management.models import OrderWorker

        create_request = {
            "name": "deepak",
            "email": "kapeed2091@gmail.com",
            "company_name": "iB"
        }
        create_response = Worker.create(**create_request)
        worker_id = create_response['worker_id']

        create_order_request = {
            "title": "Test title",
            "description": "Test description",
            "deadline": "2018-09-20"
        }
        create_order_response = Order.create(**create_order_request)
        order_id = create_order_response['order_id']

        assign_worker_request = {
            "order_id": order_id,
            "worker_id": worker_id
        }
        Order.assign_worker(**assign_worker_request)

        request = {"worker_id": worker_id}
        expected_response = [
            {
                "order_id": 1,
                "title": "Test title",
                "description": "Test description",
                "deadline": datetime.date(2018, 9, 20)
            }
        ]
        actual_response = OrderWorker.fetch_orders(**request)

        self.assertEqual(actual_response, expected_response,
                         'Error in GetWorkOrdersTest.testcase_01')
