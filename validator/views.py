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
        return Response(
            {
                "filled": response[0],
                "partially_filled": response[1],
                "trigger": response[2],
                "parameters": response[3],
            },
        )
