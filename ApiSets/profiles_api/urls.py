from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api.views import UserProfileViewset, UserLoginApiView

router = DefaultRouter()
router.register('profile', UserProfileViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('login', UserLoginApiView.as_view()),
]