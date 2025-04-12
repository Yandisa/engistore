from django.urls import path
from . import views

# URL patterns for the Asset app
urlpatterns = [
    # Lists all registered assets
    path('', views.asset_list, name='asset_list'),

    # Shows details for a single asset by primary key
    path(
        '<int:pk>/',
        views.asset_detail,
        name='asset_detail'
    ),
]
