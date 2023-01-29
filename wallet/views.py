# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from http import HTTPStatus

from django.http import JsonResponse
from rest_framework import viewsets

from .address_generator import generate_address
from .models import Wallet
from .serializers import WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()

    def create(self, request):
        address = generate_address(request.data)

        wallet = Wallet(**request.data, address=address)
        wallet.save()

        return JsonResponse(self.serializer_class(wallet).data, status=HTTPStatus.CREATED)
