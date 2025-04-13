from django.urls import path
from .views import create_user, CustomLoginView

# URL patterns for user-related actions
urlpatterns = [
    # 🧑‍💼 Create a new user (Admin/Manager only)
    path('create/', create_user, name='create_user'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
