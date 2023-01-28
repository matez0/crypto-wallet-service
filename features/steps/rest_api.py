# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

import json
import os
from subprocess import Popen, STDOUT
from time import sleep

from behave import given, then, when
import requests

from environment import django_manage_commandline

SERVER_URL = 'http://127.0.0.1:8000'


@given(u'the service is started')
def step_impl(context):
    context.service_process = Popen(django_manage_commandline('runserver'))
    context.add_cleanup(context.service_process.terminate)
    sleep(5)


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
