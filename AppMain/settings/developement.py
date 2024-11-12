import sys
from ._partials import *
# https://testdriven.io/blog/django-static-files/
# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

# MIDDLEWARE.append("whitenoise.middleware.WhiteNoiseMiddleware",)

# STATIC_HOST = "https://d4663kmspf1sqa.cloudfront.net" if not DEBUG else ""
# STATIC_URL = STATIC_HOST + "/static/"

# STATIC_HOST = os.environ.get("DJANGO_STATIC_HOST", "")
# STATIC_URL = STATIC_HOST + "/static/"
# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

# if sys.argv[1] == "collectstatic" or not DEBUG:
#     STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# else:
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, "static")
#     ]


if len(sys.argv) > 1 and sys.argv[1] == "collectstatic" or not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "static/")
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static")
    ]
