"""
"""
from rest_framework import serializers
from numbers4.models import Numbers4


class Numbers4Serialiser(serializers.ModelSerializer):
    class Meta:
        model = Numbers4