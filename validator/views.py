from rest_framework import mixins, generics
from rest_framework.response import Response

from .serializers import FiniteValuesEntitySerializer, NumericEntitySerializer
from .utils import Validator


class FiniteValuesEntityView(generics.GenericAPIView):
    serializer_class = FiniteValuesEntitySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not (serializer.is_valid()):
            return Response(serializer.errors)

        new_validator = Validator()
        response = new_validator.validate_finite_values_entity(**serializer.data)
        return Response(new_validator.format_response(response))


class NumericEntityView(generics.GenericAPIView):
    serializer_class = NumericEntitySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not (serializer.is_valid()):
            return Response(serializer.errors)

        new_validator = Validator()
        response = new_validator.validate_numeric_entity(**serializer.data)
        return Response(new_validator.format_response(response))