from rest_framework import serializers


class GetWorkOrdersResponseType:
    def __init__(self, order_id, title, description, deadline):
        self.order_id = order_id
        self.title = title
        self.description = description
        self.deadline = deadline


class GetWorkOrdersResponseSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    deadline = serializers.DateField()

    def create(self, validated_data):
        return GetWorkOrdersResponseType(**validated_data)
