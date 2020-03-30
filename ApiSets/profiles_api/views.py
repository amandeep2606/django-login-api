from django.shortcuts import render
from profiles_api.models import UserProfile
from profiles_api.serializers import UserProfileSerializer
from profiles_api.permissions import UpdateOwnProfile
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

# Create your views here.


class UserProfileViewset(viewsets.ModelViewSet):
    """
    viiewset for UserProfile Model
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """
    handle creating user authentication
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


