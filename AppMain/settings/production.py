# import sys
from ._partials import *

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
