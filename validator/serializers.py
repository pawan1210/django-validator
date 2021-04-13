from rest_framework import serializers


class CommonSerializer(serializers.Serializer):
    invalid_trigger = serializers.CharField(required=True)
    key = serializers.CharField(required=True, max_length=200)
    reuse = serializers.BooleanField(default=True)
    support_multiple = serializers.BooleanField(default=True)
    pick_first = serializers.BooleanField(default=False)
    type = serializers.ListField(required=True, allow_empty=True)
    validation_parser = serializers.CharField(required=True, max_length=200)
    values = serializers.ListField(required=True, allow_empty=True)


class FiniteValuesEntitySerializer(CommonSerializer):
    name = serializers.CharField(required=True, max_length=200)
    supported_values = serializers.ListField(required=True, allow_empty=True)


class NumericEntitySerializer(CommonSerializer):
    constraint = serializers.CharField(required=True, max_length=200)
    var_name = serializers.CharField(required=True, max_length=10)
