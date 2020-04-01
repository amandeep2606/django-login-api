from django.shortcuts import render
from profiles_api.models import UserProfile, ProfileFeedItem
from profiles_api.serializers import UserProfileSerializer, ProfileFeedItemSerializer
from profiles_api.permissions import UpdateOwnProfile, UpdateOwnStatus
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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


class ProfileItemFeedViewset(viewsets.ModelViewSet):
    """
    creating updating and reading profile feed items
    """
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, UpdateOwnStatus)

    def perform_create(self, serializer):
        """
        sets the user profile to logged in user
        :param serializer:
        :return:
        """
        serializer.save(user_profile=self.request.user)