from rest_framework.response import Response
from rest_framework import status


def request_response_wrapper(request_serializer_class,
                             response_serializer_class):
    def decorator(func):
        def handler(*args, **kwargs):
            request = args[0]

            if request.method == 'GET':
                request_serializer = request_serializer_class(
                    data=request.query_params)
            elif request.method == 'POST':
                request_serializer = request_serializer_class(
                    data=request.data)
            else:
                raise Exception

            if not request_serializer.is_valid():
                return Response(request_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)

            request_object = request_serializer.save()
            kwargs['request_object'] = request_object
            response = func(*args, **kwargs)

            if type(response) == Response:
                return response
            elif type(response) == list:
                response_serializer = response_serializer_class(response, many=True)
            else:
                response_serializer = response_serializer_class(response)

            return Response(response_serializer.data,
                            status=status.HTTP_200_OK)

        handler.__doc__ = func.__doc__
        return handler

    return decorator
