"""
Django settings for swiper project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ycv6h5a&=8#y$+ntv99wowh7=dwn9$g+6+oiaiu%(n5o*f6+h8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'user',
    'social',
    'vip'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'lib.middleware.AuthMiddleware',
    'lib.middleware.LogicErrMiddleware'
]
# from django.contrib.sessions.middleware import SessionMiddleware

ROOT_URLCONF = 'swiper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'swiper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sz1812',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': 3306,
        'HOST': '127.0.0.1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = 'medias'


CACHES = {
    "default": {
    "BACKEND": "django_redis.cache.RedisCache",
    "LOCATION": "redis://127.0.0.1:6379/12",
    "OPTIONS": {
    "CLIENT_CLASS": "django_redis.client.DefaultClient",
    "PICKLE_VERSION": -1,
    		}
	}
}


# 日志配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # 格式配置
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(module)s.%(funcName)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': ('%(asctime)s %(levelname)s [%(process)d-%(threadName)s] '
                    '%(module)s.%(funcName)s line %(lineno)d: %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S',
        }
    },
    # Handler 配置
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG' if DEBUG else 'WARNING'
        },
        'info': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/info.log',  # 日志保存路径
            'when': 'D',        # 每天切割日志
            'backupCount': 30,  # 日志保留 30 天
            'formatter': 'simple',
            'level': 'INFO',
        },
        'error': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{BASE_DIR}/logs/error.log',  # 日志保存路径
            'when': 'W0',      # 每周一切割日志
            'backupCount': 4,  # 日志保留 4 周
            'formatter': 'verbose',
            'level': 'WARNING',
        }
    },
    # Logger 配置
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'inf': {
            'handlers': ['info'],
            'propagate': True,
            'level': 'INFO',
        },
        'err': {
            'handlers': ['error'],
            'propagate': True,
            'level': 'WARNING',
        }
    }
}

REDIS = {
    'Master': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 6
    },
    'Slave': {
        'host': '127.0.0.1',
        'port': 6379,
        'db': 6
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'