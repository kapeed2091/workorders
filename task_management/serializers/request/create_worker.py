from rest_framework import serializers


class CreateWorkerRequestType:
    def __init__(self, name, email, company_name):
        self.name = name
        self.email = email
        self.company_name = company_name


class CreateWorkerRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    company_name = serializers.CharField()

    def create(self, validated_data):
        return CreateWorkerRequestType(**validated_data)
