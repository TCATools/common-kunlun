"""
Django settings for Kunlun_M project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import platform as platform_pack

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nothing'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web.index',
    'web.dashboard',
    'web.backend'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Kunlun_M.middleware.SDataMiddleware',
]

ROOT_URLCONF = 'Kunlun_M.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'Kunlun_M.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if os.path.isdir(os.path.join(BASE_DIR, 'db')) is not True:
    os.mkdir(os.path.join(BASE_DIR, 'db'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db', 'kunlun.db'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# templates
# 占位

# web setting
TITLE = 'KunLun-M Dashbroad'
DESCRIPTION = 'KunLun-Mirror 专注于白帽子的静态代码审计工具'
SUPER_ADMIN = []
IS_OPEN_REGISTER = True


# 全局变量配置

PROJECT_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
TMP_PATH = './tmp'
if os.path.isdir(TMP_PATH) is not True:
    os.mkdir(TMP_PATH)
RUNNING_PATH = os.path.join(PROJECT_DIRECTORY, TMP_PATH, 'running')
if os.path.isdir(RUNNING_PATH) is not True:
    os.mkdir(RUNNING_PATH)
PACKAGE_PATH = os.path.join(PROJECT_DIRECTORY, TMP_PATH, 'package')
if os.path.isdir(PACKAGE_PATH) is not True:
    os.mkdir(PACKAGE_PATH)
SOURCE_PATH = os.path.join(PROJECT_DIRECTORY, TMP_PATH, 'git')

if os.path.isdir(SOURCE_PATH) is not True:
    os.mkdir(SOURCE_PATH)

ISSUE_PATH = os.path.join(PROJECT_DIRECTORY, TMP_PATH, 'issue')
if os.path.isdir(ISSUE_PATH) is not True:
    os.mkdir(ISSUE_PATH)

EXPORT_PATH = os.path.join(PROJECT_DIRECTORY, TMP_PATH, 'export')
if not os.path.exists(EXPORT_PATH):
    os.mkdir(EXPORT_PATH)

if os.path.isdir('./result') is not True:
    os.mkdir('./result')
DEFAULT_RESULT_PATH = os.path.join(PROJECT_DIRECTORY, 'result/')

KUNLUN_MAIN = os.path.join(PROJECT_DIRECTORY, 'kunlun.py')
CORE_PATH = os.path.join(PROJECT_DIRECTORY, 'core')
TESTS_PATH = os.path.join(PROJECT_DIRECTORY, 'tests')
EXAMPLES_PATH = os.path.join(TESTS_PATH, 'examples')
RULES_PATH = os.path.join(PROJECT_DIRECTORY, 'rules')
CONFIG_PATH = os.path.join(PROJECT_DIRECTORY, 'config')
LOGS_PATH = os.path.join(PROJECT_DIRECTORY, 'logs')
PLUGIN_PATH = os.path.join(PROJECT_DIRECTORY, 'core', 'plugins')
IGNORE_PATH = os.path.join(PROJECT_DIRECTORY, 'Kunlun_M', '.kunlunmignore')

# history
HISTORY_FILE_PATH = os.path.join(PROJECT_DIRECTORY, TMP_PATH, '.history')
MAX_HISTORY_LENGTH = 1000

# check platform
PLATFORM = "Linux"
if "Windows" in platform_pack.system():
    PLATFORM = "windows"
elif "Linux" in platform_pack.system():
    PLATFORM = "linux"
elif "Darwin" in platform_pack.system():
    PLATFORM = "mac"