# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from bitcoinlib.keys import BKeyError, HDKey
from rest_framework.exceptions import ParseError


def generate_address(currency: str, private_key: str, index: int):
    if currency == 'BTC':
        try:
            hd_key = HDKey(private_key)

        except BKeyError as exc:
            raise ParseError(exc)

        return hd_key.child_private(index).address()

    else:
        raise ParseError("Invalid currency")
