from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from task_management.serializers.request.delete_worker import \
    DeleteWorkerRequestSerializer


@api_view(['POST'])
def delete_worker(request):
    request_data = request.data
    request_serializer = DeleteWorkerRequestSerializer(data=request_data)

    if request_serializer.is_valid():
        request_object = request_serializer.save()
    else:
        return Response(request_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    worker_id = request_object.worker_id

    from task_management.models import Worker
    try:
        Worker.remove(worker_id=worker_id)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response('Invalid worker_id', status=status.HTTP_400_BAD_REQUEST)
