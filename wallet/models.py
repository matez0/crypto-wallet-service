# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from django.db import models


class Wallet(models.Model):
    currency = models.CharField(max_length=3, help_text='three-letter acronym, such as “BTC” or “ETH”')
    address = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)
    index = models.IntegerField(help_text='Use different index to generate different address with the same private key')
