"""
Django settings for lichois project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-dmfjvzo)p997$m)2fn&(zw$l8o%=#w=)q(_bs23v@f=qh$6u8r"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "base_module.apps.AppConfig",
    "app.apps.AppConfig",
    "app_search.apps.AppSearchConfig",
    "app_pdf_utilities.apps.AppPdfUtilitiesConfig",
    "app_checklist.apps.AppChecklistConfig",
    "app_attachments.apps.AppAttachmentsConfig",
    "app_address.apps.AppAddressConfig",
    "app_contact.apps.AppContactConfig",
    "app_personal_details.apps.AppPersonalDetailsConfig",
    "app_comments.apps.AppCommentsConfig",
    "app_decision.apps.AppDecisionConfig",
    "workresidentpermit.apps.WorkresidentpermitConfig",
    "identifier.apps.AppConfig",
    "haystack",
    "rest_framework",
    "rest_framework_swagger",
    "drf_yasg",  # Yet Another Swagger generator
    "viewflow",
    "viewflow.workflow",
    #"django_filters",
    "django_api_client",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lichois.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lichois.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/app',
        'ADMIN_URL': 'http://127.0.0.1:8983/solr/admin/cores',
        'TIMEOUT': 60 * 5
    },
}

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Your React app's URL
    'http://localhost:8000',
    'http://localhost:5173'
]

# DJANGO_API_CLIENT = {
#   'API': [
#     # {
#     #     'NAME': 'production',
#     #     'BASE_URL': 'https://example.com',
#     #     'ENDPOINTS': [
#     #         '/v1/order/orders',
#     #         '/v1/user/users',
#     #         ...
#     #     ],
#     #     'AUTHENTICATION_ACCESS_TOKEN': 'TOKEN'
#     # },
#     {
#         'NAME': 'localhost',
#         'BASE_URL': 'http://localhost:8001',
#         'ENDPOINTS': [
#             '/v1/order/orders',
#             '/v1/user/users',
#             ...
#         ],
#         'AUTHENTICATION_ACCESS_TOKEN': 'TOKEN'
#     }
#   ]
# }
