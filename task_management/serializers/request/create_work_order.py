from rest_framework import serializers


class CreateWorkOrderRequestType:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline


class CreateWorkOrderRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    deadline = serializers.DateField()

    def create(self, validated_data):
        return CreateWorkOrderRequestType(**validated_data)
