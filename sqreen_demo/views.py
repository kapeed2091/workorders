from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


@api_view(['POST'])
def webhook(request):
    from sqreen_demo.constants import SQREEN_SECRET_KEY

    request_signature = request.headers['X-Sqreen-Integrity']
    request_body = request.stream.read()

    signature_status = check_signature(
        SQREEN_SECRET_KEY, request_signature,request_body)

    return get_response(signature_status)


def check_signature(secret_key, request_signature, request_body):
    import hashlib
    import hmac

    hasher = hmac.new(secret_key, request_body, hashlib.sha256)
    dig = hasher.hexdigest()

    return hmac.compare_digest(dig, request_signature)


def get_response(signature_status):
    if signature_status:
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
