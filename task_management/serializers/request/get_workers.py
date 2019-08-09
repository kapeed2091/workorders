from rest_framework import serializers


class GetWorkersRequestType:
    def __init__(self, offset, limit):
        self.offset = offset
        self.limit = limit


class GetWorkersRequestSerializer(serializers.Serializer):
    offset = serializers.IntegerField()
    limit = serializers.IntegerField()

    def create(self, validated_data):
        return GetWorkersRequestType(**validated_data)
