from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import NumbersSerializer
from .models import RequestLog


class SortNumbersView(APIView):
    """SortNumbersView handles POST requests to sort a list of numbers.
    Methods:
        post(request): Validates and sorts the list of numbers from the request data.
    swagger_auto_schema: Automatically generates Swagger documentation for the API endpoint.
    """
    @swagger_auto_schema(
        request_body=NumbersSerializer,
        responses={200: openapi.Response('Sorted numbers', NumbersSerializer)},
    )
    def post(self, request):
        """
        Handle POST request to sort a list of numbers.
        This method receives a POST request containing a list of numbers,
        validates the data using NumbersSerializer, sorts the numbers,
        logs the request and response, and returns the sorted list.
        Args:
            request (Request): The HTTP request object containing the data to be sorted.
        Returns:
            Response: A Response object containing the sorted list of numbers
                      and an HTTP status code 200 if the data is valid,
                      otherwise a Response object containing the validation errors
                      and an HTTP status code 400.
        """
        serializer = NumbersSerializer(data=request.data)
        if serializer.is_valid():
            sorted_numbers = sorted(serializer.validated_data['numbers'])
            response_data = {'sorted_numbers': sorted_numbers}

            # Log request and response
            RequestLog.objects.create(
                request_body=request.data,
                response_body=response_data
            )
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)