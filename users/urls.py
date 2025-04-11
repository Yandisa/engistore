from django.urls import path
from .views import create_user

# URL patterns for user-related actions
urlpatterns = [
    path(
        'create/',
        create_user,
        name='create_user'
    ),
]
