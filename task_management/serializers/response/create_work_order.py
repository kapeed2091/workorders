from rest_framework import serializers


class CreateWorkOrderResponseType:
    def __init__(self, order_id):
        self.order_id = order_id


class CreateWorkOrderResponseSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()

    def create(self, validated_data):
        return CreateWorkOrderResponseType(**validated_data)
