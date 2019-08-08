from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from task_management.serializers.request.create_worker import \
    CreateWorkerRequestSerializer
from task_management.serializers.response.create_worker import \
    CreateWorkerResponseType, CreateWorkerResponseSerializer


@api_view(['POST'])
def create_worker(request):
    request_data = request.data
    request_serializer = CreateWorkerRequestSerializer(data=request_data)

    if request_serializer.is_valid():
        request_object = request_serializer.save()
    else:
        return Response(request_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    name = request_object.name
    email = request_object.email
    company_name = request_object.company_name

    from task_management.models import Worker
    response_dict = Worker.create(
        name=name, email=email, company_name=company_name)

    response_type = CreateWorkerResponseType(**response_dict)
    response_serializer = CreateWorkerResponseSerializer(response_type)
    return Response(response_serializer.data, status=status.HTTP_200_OK)
