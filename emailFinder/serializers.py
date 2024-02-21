from rest_framework import serializers
from .models import FinderModel



class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinderModel
        fields = ['web_list', 'emails']