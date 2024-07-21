from rest_framework import serializers

class FilterSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, allow_blank=True)
    industry = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    country = serializers.CharField(required=False, allow_blank=True)
    year_founded = serializers.CharField(required=False, allow_blank=True)
    employees_from = serializers.CharField(required=False, allow_blank=True)
    employees_to = serializers.CharField(required=False, allow_blank=True)
