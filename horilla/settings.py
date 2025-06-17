import os
import dj_database_url
from os.path import join
from pathlib import Path
import environ
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "unsafe-default"),
    ALLOWED_HOSTS=(list, ["*"]),
    CSRF_TRUSTED_ORIGINS=(list, []),
    TIME_ZONE=(str, "Asia/Kolkata"),
)

# Load .env file for local dev
env.read_env(os.path.join(BASE_DIR, ".env"), overwrite=True)

SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = env("ALLOWED_HOSTS")
CSRF_TRUSTED_ORIGINS = env("CSRF_TRUSTED_ORIGINS")

DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'TestDB_Horilla.sqlite3')}",
        conn_max_age=600,
        ssl_require=not DEBUG,
    )
}

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# Secure settings for production
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
