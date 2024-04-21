from rest_framework import serializers
from lichois.visa.models import ContactMethod


class ContactMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMethod
        fields = '__all__'
