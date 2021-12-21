# coding: utf-8
#
# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import WalletViewSet

router = DefaultRouter()
router.register(r"wallet", WalletViewSet)

urlpatterns = [
    path("", include(router.urls))
]
