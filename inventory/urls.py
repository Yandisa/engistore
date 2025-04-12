"""
URL patterns for inventory-related views.

Includes part browsing, detail view, part request submission,
user request history, and about page.
"""

from django.urls import path
from . import views

urlpatterns = [
    # 🧾 List all parts
    path('', views.part_list, name='part_list'),

    # 🔍 Detail view for a specific part
    path('<int:pk>/', views.part_detail, name='part_detail'),

    # 📩 Submit a part request (for missing inventory)
    path('request-part/', views.request_part, name='request_part'),

    # 📝 View all requests by the logged-in user
    path('my-requests/', views.my_part_requests, name='my_part_requests'),

    # 📘 About page for EngiStore system overview
    path('about/', views.about, name='about'),
]
