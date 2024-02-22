from rest_framework import serializers
from .models import FinderModel, SortingModel


# create a serializer for the scrapping project
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinderModel
        fields = ['emails']

#Create a serializer for the email sorting project
class SortingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortingModel
        fields = ['email']
