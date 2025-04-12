from django.urls import path
from .views import create_user

# URL patterns for user-related actions
urlpatterns = [
    # 🧑‍💼 Create a new user (Admin/Manager only)
    path('create/', create_user, name='create_user'),
]
