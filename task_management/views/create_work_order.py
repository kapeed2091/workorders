from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from task_management.serializers.request.create_work_order import \
    CreateWorkOrderRequestSerializer
from task_management.serializers.response.create_work_order import \
    CreateWorkOrderResponseType, CreateWorkOrderResponseSerializer


@api_view(['POST'])
def create_work_order(request):
    request_data = request.data
    request_serializer = CreateWorkOrderRequestSerializer(data=request_data)

    if request_serializer.is_valid():
        request_object = request_serializer.save()
    else:
        return Response(request_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    title = request_object.title
    description = request_object.description
    deadline = request_object.deadline

    from task_management.models import Order
    response_dict = Order.create(title=title, description=description,
                                 deadline=deadline)

    response_type = CreateWorkOrderResponseType(**response_dict)
    response_serializer = CreateWorkOrderResponseSerializer(response_type)
    return Response(response_serializer.data, status=status.HTTP_200_OK)
