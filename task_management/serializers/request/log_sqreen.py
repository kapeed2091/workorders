from rest_framework import serializers


class LogSqreenRequestType:
    def __init__(self, data):
        self.data = data


class LogSqreenRequestSerializer(serializers.Serializer):
    data = serializers.CharField()

    def create(self, validated_data):
        return LogSqreenRequestType(**validated_data)
