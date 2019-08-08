from rest_framework import serializers


class CreateWorkerResponseType:
    def __init__(self, worker_id):
        self.worker_id = worker_id


class CreateWorkerResponseSerializer(serializers.Serializer):
    worker_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreateWorkerResponseType(**validated_data)
