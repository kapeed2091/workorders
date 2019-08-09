from rest_framework.decorators import api_view
from task_management.serializers.request.get_workers import \
    GetWorkersRequestSerializer
from task_management.serializers.response.get_workers import \
    GetWorkersResponseType, GetWorkersResponseSerializer
from task_management.request_response_decorator import request_response_wrapper


@api_view(['POST'])
@request_response_wrapper(GetWorkersRequestSerializer,
                          GetWorkersResponseSerializer)
def get_workers(request, **kwargs):
    request_object = kwargs['request_object']
    offset = request_object.offset
    limit = request_object.limit

    from task_management.models import Worker
    workers = Worker.get(offset, limit)

    response = [GetWorkersResponseType(**worker) for worker in workers]
    return response
