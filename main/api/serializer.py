from rest_framework import serializers
from main.models import University, Degree, Mdata


class UniModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = "__all__"


class DegModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"


class MdataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mdata
        fields = "__all__"
