from rest_framework import serializers


class GetWorkersResponseType:
    def __init__(self, worker_id, name, email, company_name):
        self.worker_id = worker_id
        self.name = name
        self.email = email
        self.company_name = company_name


class GetWorkersResponseSerializer(serializers.Serializer):
    worker_id = serializers.IntegerField()
    name = serializers.CharField()
    email = serializers.EmailField()
    company_name = serializers.CharField()

    def create(self, validated_data):
        return GetWorkersResponseType(**validated_data)
