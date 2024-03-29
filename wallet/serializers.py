# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from rest_framework import serializers

from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = ['private_key', 'index']


class CreateWalletRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        exclude = ["address"]
