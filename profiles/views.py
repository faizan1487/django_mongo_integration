from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.db import IntegrityError
from rest_framework.response import Response

class UserProfileListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
