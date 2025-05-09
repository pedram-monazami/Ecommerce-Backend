from rest_framework import serializers

from landing.models import *


class LocationSerializer(serializers.ModelSerializer):
    """
    Location model serializer
    """

    class Meta:
        model = Location
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """
    Contact model serializer
    """

    class Meta:
        model = Contact
        fields = [
            'sender_email',
            'subject',
            'content',
            'location'
        ]

    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())

