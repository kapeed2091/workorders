from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from task_management.serializers.request.log_sqreen import \
    LogSqreenRequestSerializer
from task_management.request_response_decorator import request_response_wrapper


@api_view(['POST'])
@request_response_wrapper(LogSqreenRequestSerializer, None)
def log_sqreen(request, **kwargs):
    request_object = kwargs['request_object']
    data = request_object.data

    from sqreen_demo.models import SqreenLog
    SqreenLog.create(data)

    return Response(status=status.HTTP_200_OK)
