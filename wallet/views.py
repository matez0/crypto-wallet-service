# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

import json

from bitcoinlib.keys import BKeyError, HDKey
from rest_framework import viewsets
from rest_framework.exceptions import ParseError

from .models import Wallet
from .serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()

    def create(self, request):
        if request.data['currency'] == 'BTC':
            request.data['address'] = generate_address_for_btc(request.data)

        else:
            raise ParseError("Invalid currency")

        response = super().create(request)
        response.data = filter_public_data(response.data)
        return response

    def list(self, request):
        response = super().list(request)
        response.data = [filter_public_data(item) for item in response.data]
        return response

    def retrieve(self, request, pk=None):
        response = super().retrieve(request)
        response.data = filter_public_data(response.data)
        return response


def generate_address_for_btc(request_data):
    try:
        hd_key = HDKey(request_data['private_key'])

    except BKeyError as e:
        raise ParseError(e)

    return hd_key.child_private(request_data['index']).address()


def filter_public_data(response_data):
    return {key: response_data[key] for key in ["id", "currency", "address"]}
