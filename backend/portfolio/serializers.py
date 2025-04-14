from rest_framework import serializers
from .models import Progetto

## SERIALIZER
class ProgettoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progetto
        fields = '__all__'
