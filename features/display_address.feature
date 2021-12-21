# Copyright (C) Zoltán Máté 2021.
# Distributed under the MIT License (license terms are at http://opensource.org/licenses/MIT).

Feature: Display cryptocurrency addresses

    Via a REST API endpoint a cryptocurrency addresses shall be displayed.

    Scenario: List addresses
        Given the service is started
        When I POST '/wallet/' to the service with JSON content:
            """
            {
                "currency": "BTC",
                "index": 0,
                "private_key": "221ff330268a9bb5549a02c801764cffbc79d5c26f4041b26293a425fd5b557c"
            }
            """
        And I POST '/wallet/' to the service with JSON content:
            """
            {
                "currency": "BTC",
                "index": 0,
                "private_key": "d02220828cad5e0e0f25057071f4dae9bf38720913e46a596fd7eb8f83ad045d"
            }
            """
        And I GET '/wallet/' from the service
        Then I get a response 200 with JSON content:
            """
            [
                {
                    "id": 1, "currency": "BTC", "address": "1MMAjrRaoje4C9VrHN7BH4vGTmhGyNgGeE"
                },
                {
                    "id": 2, "currency": "BTC", "address": "1KWaAehZBWytWA2h2bt1shPtsG9a59NFZW"
                }
            ]
            """

    Scenario: Retrieve an address
        Given the service is started
        When I POST '/wallet/' to the service with JSON content:
            """
            {
                "currency": "BTC",
                "index": 0,
                "private_key": "221ff330268a9bb5549a02c801764cffbc79d5c26f4041b26293a425fd5b557c"
            }
            """
        And I GET '/wallet/1/' from the service
        Then I get a response 200 with JSON content:
            """
            {
                "id": 1, "currency": "BTC", "address": "1MMAjrRaoje4C9VrHN7BH4vGTmhGyNgGeE"
            }
            """
