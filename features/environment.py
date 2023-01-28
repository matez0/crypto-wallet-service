from subprocess import run


def django_manage_commandline(command):
    return f'python manage.py {command}'.split()


def before_all(context):
    setup_service()


def setup_service():
    run(django_manage_commandline('makemigrations'))

    run(django_manage_commandline('migrate'))


def before_scenario(context, scenario):
    empty_db()


def empty_db():
    run(django_manage_commandline('flush --no-input'))
