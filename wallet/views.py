# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from http import HTTPStatus

from django.http import JsonResponse
from rest_framework import viewsets

from .models import Wallet
from .serializers import CreateWalletRequestSerializer, WalletSerializer


class WalletViewSet(viewsets.ModelViewSet):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()

    def create(self, request):
        data = CreateWalletRequestSerializer(request.data).data

        wallet = Wallet.create(**data)

        return JsonResponse(self.serializer_class(wallet).data, status=HTTPStatus.CREATED)
