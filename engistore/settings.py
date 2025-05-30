import os
import sys
from pathlib import Path
from django.urls import reverse_lazy

# 📁 Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))  # Add project to Python path

# 🔐 Security
SECRET_KEY = os.getenv("SECRET_KEY", "fallback-insecure-dev-key")
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
ALLOWED_HOSTS = ['*']

# 📦 Installed applications
INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🌟 Custom apps
    'inventory',
    'assets',
    'suppliers',
    'users',
    'core',
]

# 🧱 Middleware
MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Static files
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔗 URL config
ROOT_URLCONF = 'engistore.urls'

# 🎨 Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'engistore.context_processors.global_debug',
            ],
        },
    },
]

# 🚀 WSGI application
WSGI_APPLICATION = 'engistore.wsgi.application'

# 🗃️ Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        )
    },
]

# 🌍 Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🖼️ Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# 🔑 Default auto primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 🔁 Redirects
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGOUT_REDIRECT_URL = reverse_lazy('login')
LOGIN_URL = 'login'

# 🛡️ CSRF Protection (for Render)
CSRF_TRUSTED_ORIGINS = [
    'https://engistore.onrender.com',
]
