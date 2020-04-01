from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    checks if user is updating its own profile
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """
    allows user to update its own status
    """

    def has_object_permission(self, request, view, obj):
        """
        check if user is trying to update its own status
        :param request:
        :param view:
        :param obj:
        :return:
        """

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
