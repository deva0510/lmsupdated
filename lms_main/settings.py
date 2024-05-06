
"""
Django settings for worktride project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-65!wki4t(64h460c1er)wf*hemi67$&v(8pf90op6-vib&-^nr'

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
    'django.contrib.humanize',
    'learning',
    'rest_framework',
    'mathfilters',
    'ckeditor',
    'ckeditor_uploader',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lms_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'lms_main.wsgi.application'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 

CKEDITOR_CONFIGS = {
    'default': {
        # Toolbar configuration
        # name - Toolbar name
        # items - The buttons enabled in the toolbar
        'toolbar_DefaultToolbarConfig': [
            {
                'name': 'basicstyles',
                'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript',
                          'Superscript', ],
            },
            {
                'name': 'clipboard',
                'items': ['Undo', 'Redo', ],
            },
            {
                'name': 'paragraph',
                'items': ['NumberedList', 'BulletedList', 'Outdent', 'Indent',
                          'HorizontalRule', 'JustifyLeft', 'JustifyCenter',
                          'JustifyRight', 'JustifyBlock', ],
            },
            {
                'name': 'format',
                'items': ['Format', ],
            },
            {
                'name': 'extra',
                'items': ['Link', 'Unlink', 'Blockquote', 'Image', 'Table',
                          'CodeSnippet', 'Mathjax', 'Embed', ],
            },
            {
                'name': 'source',
                'items': ['Maximize', 'Source', ],
            },
        ],

        # This hides the default title provided by CKEditor
        'title': False,

        # Use this toolbar
        'toolbar': 'DefaultToolbarConfig',

        # Which tags to allow in format tab
        'format_tags': 'p;h1;h2',

        # Remove these dialog tabs (semicolon separated dialog:tab)
        'removeDialogTabs': ';'.join([
            'image:advanced',
            'image:Link',
            'link:upload',
            'table:advanced',
            'tableProperties:advanced',
        ]),
        'linkShowTargetTab': False,
        'linkShowAdvancedTab': False,

        # CKEditor height and width settings
        'height': '250px',
        'width': 'auto',
        'forcePasteAsPlainText ': True,

        # Class used inside span to render mathematical formulae using latex
        'mathJaxClass': 'mathjax-latex',

        # Mathjax library link to be used to render mathematical formulae
        'mathJaxLib': 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_SVG',

        # Tab = 4 spaces inside the editor
        'tabSpaces': 4,

        # Extra plugins to be used in the editor
        'extraPlugins': ','.join([
            'devtools',  # Shows a tooltip in dialog boxes for developers
            'mathjax',  # Used to render mathematical formulae
            'codesnippet',  # Used to add code snippets
            'image2',  # Loads new and better image dialog
            'embed',  # Used for embedding media (YouTube/Slideshare etc)
            'tableresize',  # Used to allow resizing of columns in tables
        ]),
    }
}





DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'lms123',
        'HOST':'sample1.mysql.database.azure.com',
        'PORT':'3306',
        'USER':"admin123",
        "PASSWORD":"Devarajulu@1998",
        'OPTIONS': {
                     "init_command": "SET foreign_key_checks = 0;",
                     
                 },
    }
}

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




LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False




STATIC_URL = 'static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

AUTH_USER_MODEL="learning.CustomUser"
AUTHENTICATION_BACKENDS=(('django.contrib.auth.backends.ModelBackend'),)

EMAIL_BACKEND="django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH=os.path.join(BASE_DIR,"sent_mails")



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MEDIA_URL="/media/"

MEDIA_ROOT=os.path.join(BASE_DIR,"media")

X_FRAME_OPTIONS='SAMEORIGIN'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'developtrees1@gmail.com'
EMAIL_HOST_PASSWORD = 'qvwqbjcxpvaysbjk'

RAZORPAY_KEY_ID = os.environ.get("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.environ.get("RAZORPAY_KEY_SECRET")

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_UPLOAD_PATH = "uploads/"


CKEDITOR_UPLOAD_PATH = "uploads/"  # Define where to upload files.
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',  # Define the toolbar configuration.
        'height': 300,  # Define the height of the editor.
        'width': 800,  # Define the width of the editor.
    },
}


# settings.py

# Your existing Django settings...

# Google OAuth 2.0 credentials
# GOOGLE_CLIENT_ID = '1040407827998-a276q1aj7oiga1a96gi4t1qelcgqc975.apps.googleusercontent.com'
# GOOGLE_CLIENT_SECRET = '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'

# Other Django settings...

# credentials_path = os.path.join(BASE_DIR, r'C:\Users\DevelopTrees\Downloads\googleauth.json')
# credentials_path = os.path.join(BASE_DIR, 'C:\\Users\\DevelopTrees\\Downloads\\googleauth.json')

# ZOOM_API_KEY = os.getenv('ZOOM_API_KEY', 'lg6fA7c2RxOvgEmCb3OIBg')
# ZOOM_API_SECRET = os.getenv('ZOOM_API_SECRET', 'zplcY0ech0RAVob8bb5cowsJm8WfNDCU')

# settings.py
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

ZOOM_CLIENT_ID = os.getenv("ZOOM_CLIENT_ID")
ZOOM_CLIENT_SECRET = os.getenv("ZOOM_CLIENT_SECRET")
ZOOM_REDIRECT_URI = os.getenv("ZOOM_REDIRECT_URI")




ZOOM_CLIENT_ID = "lg6fA7c2RxOvgEmCb3OIBg"
ZOOM_CLIENT_SECRET = "zplcY0ech0RAVob8bb5cowsJm8WfNDCU"
ZOOM_REDIRECT_URI = "http://127.0.0.1:8000/zoom/callback/"


# Zoom_API_KEY = 'o2ZrdhbRBaWY6shnq87Aw'
# Zoom_API_SECRET = 'GzBs4CRE0R8QcP7531twIKKxvYrK3WEL'
# Zoom_Account_ID = 'Rcv2tke6TW-smyWtp3jrvA'
# Zoom_Role_ID = 'your_role_id'

# Add these settings, replacing the example values
