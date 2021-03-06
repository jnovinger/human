# Django settings for django_regimun project.
from django.conf import global_settings
import os
import re

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Clare Liguori', 'clare@clareliguori.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE'    : 'django.db.backends.mysql', # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME'      : 'regimundb',    # Or path to database file if using sqlite3.
        'USER'      : 'regimunuser',  # Not used with sqlite3.
        'PASSWORD'  : 'kof1UN12#',    # Not used with sqlite3.
        'HOST'      : '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT'      : '',             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/clare/Programming/regimun/public/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sw27fxjh!y!6%o1deue6m_=6u%-0(pqblrum$$5d(6z_i(d^dr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.eggs.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ('django.core.context_processors.request',
                               'django.contrib.auth.context_processors.auth',
                               'django.core.context_processors.debug',
                               'django.core.context_processors.i18n',
                               'django.core.context_processors.media',
                               'django.contrib.messages.context_processors.messages')

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
  #  'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'django_regimun.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.abspath(os.path.dirname(__file__)), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
  #  'debug_toolbar',
    'regimun_app',
)

FILE_UPLOAD_HANDLERS = ('regimun_app.utils.UploadProgressCachedHandler', ) + \
    global_settings.FILE_UPLOAD_HANDLERS

AUTH_PROFILE_MODULE = ''

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

DEFAULT_FROM_EMAIL='info@munsoftware.com'
EMAIL_HOST="localhost"
SERVER_EMAIL=DEFAULT_FROM_EMAIL

SEND_BROKEN_LINK_EMAILS=True
IGNORABLE_404_URLS = (
        re.compile(r'^/apple-touch-icon.*\.png$'),
        re.compile(r'^/favicon\.ico$'),
        re.compile(r'^/robots\.txt$'),
	re.compile(r'country_flags.*\.png$'),
)

IGNORABLE_404_ENDS = ('favicon.ico', 'apple-touch-icon.png', 'robots.txt')
IGNORABLE_404_STARTS = (MEDIA_URL+'/country_flags/')

#INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

if DEBUG:
    TEMPLATE_STRING_IF_INVALID = "BAD TEMPLATE"
else:
    TEMPLATE_STRING_IF_INVALID = ''

ENABLE_CAPTCHA = True

TEST_RUNNER = 'django-test-coverage.runner.run_tests'
