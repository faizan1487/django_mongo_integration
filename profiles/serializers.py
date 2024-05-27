from rest_framework import serializers
from .models import UserProfile
from .fields import ObjectIdField

class UserProfileSerializer(serializers.ModelSerializer):
    id = ObjectIdField(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'name', 'email', 'bio', 'created_at', 'updated_at']
