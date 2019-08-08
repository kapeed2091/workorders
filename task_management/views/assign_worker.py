from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from task_management.serializers.request.assign_worker import \
    AssignWorkerRequestSerializer


@api_view(['POST'])
def assign_worker(request):
    request_data = request.data
    request_serializer = AssignWorkerRequestSerializer(data=request_data)

    if request_serializer.is_valid():
        request_object = request_serializer.save()
    else:
        return Response(request_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    order_id = request_object.order_id
    worker_id = request_object.worker_id

    from task_management.models import Order, Worker

    if not Order.is_valid(order_id):
        return Response('Invalid order_id', status=status.HTTP_400_BAD_REQUEST)

    if not Worker.is_valid(worker_id):
        return Response('Invalid worker_id',
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        Order.assign_worker(order_id=order_id, worker_id=worker_id)
    except:
        return Response('Order cannot have more than 5 workers',
                        status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_200_OK)
