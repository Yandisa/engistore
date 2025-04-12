"""
Root URL configuration for EngiStore.

Includes routes for admin, dashboard, apps, authentication,
and user management.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from inventory.views import dashboard

urlpatterns = [
    # 🔐 Admin panel
    path('admin/', admin.site.urls),

    # 🏠 Dashboard (landing page after login)
    path('', dashboard, name='dashboard'),

    # 📦 Inventory management
    path('inventory/', include('inventory.urls')),

    # 🛠 Assets tracking
    path('assets/', include('assets.urls')),

    # 👥 User-related views (e.g., create user)
    path('users/', include('users.urls')),

    # 🔐 Auth (login, logout, password reset, etc.)
    path('accounts/logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
