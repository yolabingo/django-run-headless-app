from pathlib import Path

import emoji

# APP_NAME of the app you want to create and/or test
APP_NAME = "change_app_name"

# add dependencies of APP_NAME to APP_DEPENDENCIES, e.g. 'rest_framework'
APP_DEPENDENCIES = []

PROJECT_ROOT_DIR = Path(__file__).parent.parent
APP_DIR = PROJECT_ROOT_DIR / APP_NAME
FIXTURES_DIR = APP_DIR / "fixtures"
TEST_DB_PATH = APP_DIR / "django-tasks-temp-db.sqlite3"

ADMIN_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sessions",
]


def print_status(message, error=False):
    if error:
        print(f"{emoji.emojize(':cross_mark:')} {message}")
    else:
        f"{emoji.emojize(':right_arrow:')} Running on DB:\n  {TEST_DB_PATH}"
        print(f"{emoji.emojize(':check_mark_button:')} {message}")
