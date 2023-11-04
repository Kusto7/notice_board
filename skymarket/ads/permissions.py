from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Класс пермишина, который ограничивает пользователям функциональность CRUD
    """

    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение (GET, HEAD, OPTIONS) доступно всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешение на запись (PUT, PATCH, DELETE) доступно только автору
        return obj.author == request.user
