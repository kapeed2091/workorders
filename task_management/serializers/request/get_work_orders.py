from rest_framework import serializers


class GetWorkOrdersRequestType:
    def __init__(self, worker_id):
        self.worker_id = worker_id


class GetWorkOrdersRequestSerializer(serializers.Serializer):
    worker_id = serializers.IntegerField()

    def create(self, validated_data):
        return GetWorkOrdersRequestType(**validated_data)
