import os
from pathlib import Path

class SERVER_DIRS:
    BASE_DIR = Path(__file__).resolve().parent.parent
    FE_STATIC = os.path.join(BASE_DIR, 'frontend/static')
    FE_BUILD = os.path.join(BASE_DIR, 'frontend/build')
    FE_BUILD_STATIC = os.path.join(BASE_DIR, 'frontend/build/static')