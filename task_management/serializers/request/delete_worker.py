from rest_framework import serializers


class DeleteWorkerRequestType:
    def __init__(self, worker_id):
        self.worker_id = worker_id


class DeleteWorkerRequestSerializer(serializers.Serializer):
    worker_id = serializers.IntegerField()

    def create(self, validated_data):
        return DeleteWorkerRequestType(**validated_data)
