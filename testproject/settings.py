# Django settings for unit test project.
import os
import sys

DEBUG = True
SITE_ID = 1
SECRET_KEY = 'secret'
LANGUAGE_CODE = 'de'
LANGUAGES = [
    ('de', 'De'),
    ('en', 'En'),
    ('fr', 'Fr'),
    ('it', 'It'),
]

APP_ROOT = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    "..",
)
)
PROJECT_ROOT = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..',
    )
)
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

sys.path.insert(0, APP_ROOT + "/../")
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'storage', 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'storage', 'static')
STATIC_URL = '/static/'
ROOT_URLCONF = 'testproject.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'data', 'database.sqlite')
    },
}

INSTALLED_APPS = [
    'testproject',
    'tac',
    'compressor',
    'text_ckeditor',

    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # CMS
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_admin_style',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'tac.middleware.TACMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, 'testproject', 'templates'),
            os.path.join(PROJECT_ROOT, 'testproject', 'templates', 'errors'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},  # NOQA
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},  # NOQA
]

# =============================================================================
# CMS Templates
# =============================================================================

CMS_TEMPLATES = (
    ('cms/default.html', 'standard page'),
)


# =============================================================================
# GENERAL CMS Settings
# =============================================================================

TEXT_CKEDITOR_LINK_MODEL = 'tac.PopupLink'


CMS_MENU_DEBUG = False  # Prints out menu nodes and their properties
CMS_CACHE_DURATIONS = {
    'content': 0,
    'menus': 0,
    'permissions': 0,
}
CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': 'De',
            'fallbacks': ['fr', 'it', 'en'],
        },
        {
            'code': 'fr',
            'name': 'Fr',
            'fallbacks': ['de', 'it', 'en'],
        },
        {
            'code': 'it',
            'name': 'Italiano',
            'fallbacks': ['de', 'fr', 'en'],
        },
        {
            'code': 'en',
            'name': 'English',
            'fallbacks': ['de', 'fr', 'it'],
        },

    ],
    'default': {
        'fallbacks': ['de', 'fr', 'it', 'en'],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}
CMS_MENU_TITLE_OVERWRITE = True
CMS_REDIRECTS = True
CMS_URL_OVERWRITE = False
