from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key
from dotenv import load_dotenv

load_dotenv()



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Templates directory setting
TEMPLATE_DIR = BASE_DIR / 'templates'  # templatesを利用できるようにする処理1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-ebsr_w6)jskcq8e#nn)6txa3q5n(xs9p0=bqh7l*%78o9^ery!'

try:
    from .local_settings import *
    DEBUG = True
    FRONTEND_URL = 'http://127.0.0.1:8000/'
    ALLOWED_HOSTS = []

except ImportError:
    DEBUG = False
    SECRET_KEY = get_random_secret_key()
    ALLOWED_HOSTS = ['.pythonanywhere.com']

PASSWORD = os.getenv("PASSWORD")



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['localhost', '.pythonanywhere.com', 'mikimiki.pythonanywhere.com']

#下記2つはローカル環境で使う
#DEBUG = True
#ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'your-domain.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'posts',
]

AUTH_USER_MODEL = 'accounts.Users'  # accounts/models.py/Usersに指定

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mama_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],  # templatesを利用できるようにする処理2
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mama_project.wsgi.application'

LOGIN_URL = '/accounts/user_login'
LOGIN_REDIRECT_URL = '/posts/list'
LOGOUT_REDIRECT_URL = "/accounts/user_login"

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization settings
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files settings
MEDIA_ROOT = BASE_DIR / 'media'  # 画像を保存する先のディレクトリ
MEDIA_URL = '/media/'  # 画像をdjango側で読み込むためのURL設定

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

try:
    from .local_settings import *
except:
    pass
