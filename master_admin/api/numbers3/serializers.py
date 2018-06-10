"""
"""
from rest_framework import serializers
from numbers3.models import Numbers3


class Numbers3Serialiser(serializers.ModelSerializer):
    class Meta:
        model = Numbers3