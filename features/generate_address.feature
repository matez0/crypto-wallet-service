# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

Feature: Generating cryptocurrency addresses

    Via a REST API endpoint a cryptocurrency and a private key as input are taken
    and an address shall be generated for that currency.
    Each cryptocurrency is identified by its three-letter acronym,
    such as “BTC” or “ETH” for Bitcoin and Ethereum respectively.
    Choosing different index value, different address can be generated with the same private key.

    Scenario: Generating address for Bitcoin
        Given the service is started
        When I POST '/wallet/' to the service with JSON content:
            """
            {
                "currency": "BTC",
                "index": 0,
                "private_key": "221ff330268a9bb5549a02c801764cffbc79d5c26f4041b26293a425fd5b557c"
            }
            """
        Then I get a response 201 with JSON content:
            """
            {
                "id": 1,
                "currency": "BTC",
                "address": "1MMAjrRaoje4C9VrHN7BH4vGTmhGyNgGeE"
            }
            """

    Scenario Outline: Generating different address with the same private key for Bitcoin
        Given the service is started
        When I POST '/wallet/' to the service with JSON content:
            """
            {
                "currency": "BTC",
                "index": <index>,
                "private_key": "221ff330268a9bb5549a02c801764cffbc79d5c26f4041b26293a425fd5b557c"
            }
            """
        Then I get a response 201 with JSON content:
            """
            {
                "id": 1,
                "currency": "BTC",
                "address": "<address>"
            }
            """

        Examples: index and address values
            | index | address                            |
            |     1 | 16PDszGGgWaFnp4sp9WxVRwhZcgieeWRzq |
            |     2 | 19uhA6yCF1hshMU7B5AM1WDsWpWq1sXB35 |

    Scenario: Invalid currency
        Given the service is started
        When I POST '/wallet/' to the service with JSON content:
            """
            {
                "currency": "INV",
                "index": 0,
                "private_key": "221ff330268a9bb5549a02c801764cffbc79d5c26f4041b26293a425fd5b557c"
            }
            """
        Then I get a response 400 with JSON content:
            """
            {"detail": "Invalid currency"}
            """

    Scenario: Invalid private key
        Given the service is started
        When I POST '/wallet/' to the service with JSON content:
            """
            {
                "currency": "BTC",
                "index": 0,
                "private_key": "invalidkey"
            }
            """
        Then I get a response 400 with JSON content:
            """
            {"detail": "Unrecognised key format"}
            """
