from . import models
from rest_framework import serializers


class MyQuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MyQuotes
        fields = '__all__'
