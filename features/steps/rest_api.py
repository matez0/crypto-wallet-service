# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

import json
import os
from shutil import rmtree, copytree, copy
from subprocess import Popen, run, STDOUT
from time import sleep

from behave import given, then, when
import requests

SERVER_URL = 'http://127.0.0.1:8000'

PYTHON_PATH = '/usr/bin/python3'


@given(u'the service is started')
def step_impl(context):
    service_dir = install_service()
    context.service_process = Popen(django_manage_commandline('runserver'), cwd=service_dir)
    context.add_cleanup(context.service_process.terminate)
    sleep(2)


def django_manage_commandline(command):
    return f'{PYTHON_PATH} manage.py {command}'.split()


def install_service():
    service_dir = '/tmp/test-wallet-service'
    rmtree(service_dir, ignore_errors=True)
    os.mkdir(service_dir)
    for source_dir in ['django_project', 'wallet']:
        copytree(source_dir, os.path.join(service_dir, source_dir))
    copy('manage.py', service_dir)

    run(django_manage_commandline('makemigrations'), cwd=service_dir)

    run(django_manage_commandline('migrate'), cwd=service_dir)

    return service_dir


@when(u"I POST '{endpoint}' to the service with JSON content")
def step_impl(context, endpoint):
    api_url = SERVER_URL + endpoint
    json_content = json.loads(context.text)
    context.response = requests.post(api_url, json=json_content)


@then(u'I get a response {status_code} with JSON content')
def step_impl(context, status_code):
    expected_json_content = json.loads(context.text)
    print(context.response.content)
    assert context.response.status_code == int(status_code)
    assert context.response.json() == expected_json_content, f'respose: {context.response.json()}'


@when(u"I GET '{endpoint}' from the service")
def step_impl(context, endpoint):
    api_url = SERVER_URL + endpoint
    context.response = requests.get(api_url)
