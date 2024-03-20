import os
import django
from django.core.management import call_command
from invoke import task

import boot_django
from base import APP_NAME, PROJECT_ROOT_DIR, TEST_DB_PATH, print_status


@task
def createsuperuser(c):
    boot_django.boot()
    """Create a superuser for the Django admin - for testing only of course"""
    username = password = "admin"
    os.environ["DJANGO_SUPERUSER_USERNAME"] = username
    os.environ["DJANGO_SUPERUSER_PASSWORD"] = password
    os.environ["DJANGO_SUPERUSER_EMAIL"] = "admin@example.com"
    print(f"Creating superuser: '{username}' with password '{password}'...")
    try:
        call_command("createsuperuser", "--noinput")
        print_status(f"Superuser created: '{username}' with password '{password}'")
    except django.core.management.base.CommandError as e:
        print_status(f"Superuser not created: {e}", error=True)


@task
def makemigrations(c):
    boot_django.boot()
    call_command("makemigrations", APP_NAME)


@task
def migrate(c):
    makemigrations(c)
    call_command("migrate", APP_NAME)
    print_status(f"Migrations complete on {TEST_DB_PATH}")


@task
def list_model_fields(c):
    boot_django.boot()
    call_command("list_model_info", "--field-class")


@task
def list_model_methods(c):
    boot_django.boot()
    call_command("list_model_info", "--all-methods")


@task
def load_fixture(c):
    migrate(c)
    call_command("loaddata", "--app", APP_NAME, APP_NAME)


@task
def reset_db(c):
    boot_django.boot()
    call_command("reset_db", "--noinput", APP_NAME)
    print_status("Database reset")


@task
def runserver_plus(c):
    load_fixture(c)
    createsuperuser(c)
    call_command("runserver_plus")


@task
def test(c):
    boot_django.boot()
    call_command("test", APP_NAME)


def django_graph_models():
    # this doesn't work here but works in a normal Django shell
    png_file = PROJECT_ROOT_DIR / "django_models.png"
    call_command("graph_models", "django_cloud_provider_zones", "-g", "-o", png_file)
    # --rankdir BT --theme django2018 -l twopi
    print_status(f"Model graph created: {str(png_file)}")
