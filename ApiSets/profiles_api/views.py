from django.shortcuts import render
from profiles_api.models import UserProfile
from profiles_api.serializers import UserProfileSerializer
from profiles_api.permissions import UpdateOwnProfile
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class UserProfileViewset(viewsets.ModelViewSet):
    """
    viiewset for UserProfile Model
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)

