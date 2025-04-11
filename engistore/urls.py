from django.contrib import admin
from django.urls import path, include
from inventory.views import dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 🔐 Admin panel
    path('admin/', admin.site.urls),

    # 🏠 Dashboard (home page after login)
    path('', dashboard, name='dashboard'),

    # 📦 Inventory app
    path('inventory/', include('inventory.urls')),

    # 🛠 Assets app
    path('assets/', include('assets.urls')),

    # 👤 Logout (handled by Django's built-in auth views)
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 🔑 Authentication routes (login, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # 👥 Custom user-related views (like create user)
    path('users/', include('users.urls')),
]
