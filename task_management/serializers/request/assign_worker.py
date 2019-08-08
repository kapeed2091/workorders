from rest_framework import serializers


class AssignWorkerRequestType:
    def __init__(self, order_id, worker_id):
        self.order_id = order_id
        self.worker_id = worker_id


class AssignWorkerRequestSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    worker_id = serializers.IntegerField()

    def create(self, validated_data):
        return AssignWorkerRequestType(**validated_data)
