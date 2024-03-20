from re import fullmatch
from invoke import task

from tasks.base import APP_DIR, APP_NAME, print_status


@task
def start(c):
    if not APP_NAME:
        print_status("Please set APP_NAME in tasks/base.py", error=True)
        return
    app_re = r"^[a-z][a-z_]+[a-z]$"
    if not fullmatch(app_re, APP_NAME):
        print_status(f"APP_NAME '{APP_NAME}' must match regex: {app_re}", error=True)
        return
    project_name = "djangotasksprojecttemp"
    project_dir = f"/tmp/{project_name}"
    assert project_dir.startswith("/tmp"), "Please use /tmp for the project directory"
    for command in [
        f"rm -rf {project_dir}",
        f"mkdir -p {project_dir} {APP_DIR}",
        f"django-admin startproject {project_name} {project_dir}",
        f"{project_dir}/manage.py startapp {APP_NAME} {APP_DIR}",
        f"rm -rf {project_dir}",
    ]:
        print(command)
        c.run(command)
    print_status(f"Created {APP_NAME} in {APP_DIR}")
