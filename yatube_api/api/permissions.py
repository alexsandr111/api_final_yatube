from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Пермишн"""

    message = 'Ступай своей дорогой.'

    def has_object_permission(self, request, view, obj):
        """Проверка доступа к объекту"""
        return request.method in SAFE_METHODS or obj.author == request.user