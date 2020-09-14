from rest_framework import serializers
from owners.models import Owner


class OwnerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['name', 'phone_number', 'email', 'doc_number']


class OwnerSerializer(serializers.ModelSerializer):
    vehicles = serializers.StringRelatedField(many=True)

    class Meta:
        model = Owner
        fields = ['name', 'doc_number', 'vehicles', 'registration']
