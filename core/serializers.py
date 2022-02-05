from core.models import *
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('city',)


class MedicalRecordSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(queryset=City.objects.all(), slug_field='name')
    country = serializers.SlugRelatedField(queryset=Country.objects.all(), slug_field='name')

    class Meta:
        model = MedicalRecord
        fields = '__all__'


