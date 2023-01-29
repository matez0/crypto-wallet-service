# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from rest_framework import viewsets

from .address_generator import generate_address
from .models import Wallet
from .serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()

    def create(self, request):
        request.data['address'] = generate_address(request.data)

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


def filter_public_data(response_data):
    return {key: response_data[key] for key in ["id", "currency", "address"]}
