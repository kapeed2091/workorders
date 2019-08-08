from django.test import TestCase


class CreateWorkOrderTest(TestCase):

    def testcase_01(self):
        request = {
            "title": "Test title",
            "description": "Test description",
            "deadline": "2018-09-20"
        }
        expected_response = {
            "order_id": 1
        }

        from task_management.models import Order
        actual_response = Order.create(**request)

        self.assertEqual(actual_response, expected_response,
                         'Error in CreateWorkOrderTest.testcase_01')
