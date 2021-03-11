from rest_framework import serializers
from applications.database.models import Cars


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ["brand", "year"]
