# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from bitcoinlib.keys import BKeyError, HDKey
from rest_framework.exceptions import ParseError


def generate_address(request_data):
    if request_data['currency'] == 'BTC':
        try:
            hd_key = HDKey(request_data['private_key'])

        except BKeyError as e:
            raise ParseError(e)

        return hd_key.child_private(request_data['index']).address()

    else:
        raise ParseError("Invalid currency")
