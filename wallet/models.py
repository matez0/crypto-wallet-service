# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

import logging

from django.db import models

from .address_generator import generate_address

logger = logging.getLogger('django')


class Wallet(models.Model):
    currency = models.CharField(max_length=3, help_text='three-letter acronym, such as “BTC” or “ETH”')
    address = models.CharField(max_length=100)
    private_key = models.CharField(max_length=100)
    index = models.IntegerField(help_text='Use different index to generate different address with the same private key')

    @classmethod
    def create(cls, currency: str, private_key: str, index: int):
        address = generate_address(currency, private_key, index)

        logger.info("Creating wallet; currency='%s' address='%s'", currency, address)

        instance = cls(currency=currency, address=address, private_key=private_key, index=index)
        instance.save()

        return instance
