from django.urls import path
from . import views

# URL patterns for the assets app
urlpatterns = [
    path('', views.asset_list, name='asset_list'),  # List all assets
    path(
        '<int:pk>/',
        views.asset_detail,
        name='asset_detail'
    ),  # View details for a specific asset
]
