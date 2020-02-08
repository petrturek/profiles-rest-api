from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS: # zde nejdříve testujeme, jestli je metoda bezpečná, pokud ano, uživatel může páchat, co chce
            return True

        return obj.id == request.user.id # vrátí True nebo False podle toho, jestli objekt patří uživateli nebo ne


class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
