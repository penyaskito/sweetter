import os 

# Django settings for sweetter project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'      # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'sweetter.db' # Or path to database file if using sqlite3.
DATABASE_USER = ''               # Not used with sqlite3.
DATABASE_PASSWORD = ''           # Not used with sqlite3.
DATABASE_HOST = ''               # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''               # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Spain/Madrid'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.getcwd(), 'static/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'om7odj)f4_bn-djy!^tdw2!!49ip+86e98#0-(#*vzg@x4sqag'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth', 
    'django.core.context_processors.debug', 
    'django.core.context_processors.i18n', 
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'sweetter.flash.context_processor',
    'sweetter.ublogging.contexts.profile',
)

INTERNAL_IPS = ('127.0.0.1', )


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'sweetter.urls'

AUTH_PROFILE_MODULE = 'ublogging.Profile'

LOGIN_REDIRECT_URL = '/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
	'templates',    
    # Plugins add their own templates
    'contrib.groups.templates',
    'contrib.recoverpw.templates',
    'contrib.karma.templates',
    'contrib.followers.templates'
    'contrib.replies.templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
	'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    
    'django.contrib.webdesign',
    
	'sweetter.ublogging',
    'sweetter.contrib.userform',
    'sweetter.contrib.groups',
    'sweetter.contrib.recoverpw',
    'sweetter.contrib.karma',
    'sweetter.contrib.followers',
    'sweetter.contrib.replies',
    'sweetter.contrib.remove',

    'sweetter.jabberbot',
)

INSTALLED_PLUGINS = (
    'sweetter.contrib.userform.UserForm.UserForm',
    'sweetter.contrib.replies.RepliesPlugin.RepliesPlugin',
    'sweetter.contrib.groups.GroupsPlugin.GroupHooks',
    'sweetter.contrib.recoverpw.recoverplugin.Recover',
    'sweetter.contrib.karma.KarmaPlugin.KarmaCount',
    'sweetter.contrib.followers.FollowerPlugin.FollowingList',
    'sweetter.contrib.followers.FollowerPlugin.FollowerList',
    'sweetter.jabberbot.jabberplugin.JabberPlugin',
    'sweetter.contrib.remove.RemovePlugin.RemovePlugin',
)

LOGIN_URL = "/login"

# Jabberbot

JB_USER = "sbottest@jabberes.org"
JB_PASSWD = "..."

# email config
    
MSG_FROM = "terron@sweetter.net"
CONFIRMATION_MSG = """
Swetter 3.0 validation
======================

Hi %(username)s!

This email account is registered in sweetter 3.0, if you don't
register in that web service you can ignore that.

To validate your account follow this link:

http://sweetter.net/sweetter/validate/%(apikey)s

--
sweetter team

"""

RECOVERY_MSG = """
Swetter 3.0 pw recovery
=======================

Hi %(username)s!

Your receive this email because you are trying to recover your
sweetter password. If you don't ask for a password recovery then
ignore that email.

To recover your sweetter password follow this link:

http://sweetter.net/recover/validate/%(key)s

--
sweetter team

"""

