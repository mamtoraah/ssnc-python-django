from rest_framework import serializers


class NumbersSerializer(serializers.Serializer):
    """
    NumbersSerializer is a serializer for validating a list of integers.
    Attributes:
        numbers (ListField): A list of integers with a minimum length of 1. 
                             Custom error messages are provided for invalid input 
                             and empty lists.
    Error Messages:
        invalid: 'numbers must be a list of integers.'
        min_length: 'numbers must not be empty.'
    """

    numbers = serializers.ListField(
        child=serializers.IntegerField(), min_length=1,
        error_messages={
            'invalid': 'numbers must be a list of integers.',
            'min_length': 'numbers must not be empty.',
        }
    )