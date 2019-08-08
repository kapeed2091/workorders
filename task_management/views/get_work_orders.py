from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from task_management.serializers.request.get_work_orders import \
    GetWorkOrdersRequestSerializer
from task_management.serializers.response.get_work_orders import \
    GetWorkOrdersResponseType, GetWorkOrdersResponseSerializer


@api_view(['POST'])
def get_work_orders(request):
    request_data = request.data
    request_serializer = GetWorkOrdersRequestSerializer(data=request_data)

    if request_serializer.is_valid():
        request_object = request_serializer.save()
    else:
        return Response(request_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    worker_id = request_object.worker_id

    from task_management.models import OrderWorker
    orders = OrderWorker.fetch_orders(worker_id=worker_id)

    response_list = [GetWorkOrdersResponseType(**ei) for ei in orders]
    response_serializer = GetWorkOrdersResponseSerializer(
        response_list, many=True)

    return Response(response_serializer.data, status=status.HTTP_200_OK)
