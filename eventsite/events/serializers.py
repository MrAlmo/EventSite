from rest_framework import serializers
from .models import Event
from users.models import CustomUser

from registrations.models import Registration


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'title', 'date_time', 'location', 'description']

class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Registration
        fields = ['username', 'event', 'registered_at']