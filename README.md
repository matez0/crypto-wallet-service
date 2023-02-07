[![test](https://github.com/matez0/crypto-wallet-service/actions/workflows/test.yml/badge.svg)](https://github.com/matez0/crypto-wallet-service/actions)
[![Python versions](https://img.shields.io/badge/python-3.7_%7C_3.11-blue.svg)](https://www.python.org/downloads/)

# crypto-wallet-service

Generating and displaying cryptocurrency addresses

# Overview

This is a Django application for generating and displaying cryptocurrency addresses via REST API.


## Todo

- Encrypt Django database.
- Implement address generation for ETH currency (using Web3).


# Bootstrap

Install `libgmp-dev` for the Python Bitcoin Library.

Install Python 3.6 or newer.

Create a python virtual environment:
```
python -m venv .venv
```

Activate the virtual environment:
```
. .venv/bin/activate
```

Install [Python library dependencies](requirements.txt):
```
pip install --upgrade pip
pip install -r requirements.txt
```


# Usage

The application accepts the following HTTP requests:

- Create a BTC address:
```http
POST /wallet/ HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
    "currency": "BTC",
    "private_key": "221ff330268a9bb5549a02c801764cffbc79d5c26f4041b26293a425fd5b557c",
    "index": 0
}
```
Response:
```http
HTTP/1.1 201 OK
Content-Type: application/json
{
    "id": 1,
    "currency": "BTC",
    "address": "1MMAjrRaoje4C9VrHN7BH4vGTmhGyNgGeE"
}
```

- List addresses:
```http
GET /wallet/ HTTP/1.1
Host: localhost:8000
```
Response:
```http
HTTP/1.1 200 OK
Content-Type: application/json
[
    {
        "id": 1,
        "currency": "BTC",
        "address": "1MMAjrRaoje4C9VrHN7BH4vGTmhGyNgGeE"
    },
    {
        "id": 2,
        "currency": "BTC",
        "address": "16PDszGGgWaFnp4sp9WxVRwhZcgieeWRzq"
    }
]
```

- Retrieve an address with a given ID `1`:
```http
GET /wallet/1/ HTTP/1.1
Host: localhost:8000
```
Response:
```http
HTTP/1.1 200 OK
Content-Type: application/json

{
    "id": 1,
    "currency": "BTC",
    "address": "16PDszGGgWaFnp4sp9WxVRwhZcgieeWRzq"
}
```


# Test

The REST API is tested with the Python `behave` framework.

To run all tests, run
```
behave
```
from the root directory of the repository.

To run unit tests, execute:
```
python manage.py test
```


# References

[Bitpanda - What are public keys, private keys and wallet addresses?](https://www.bitpanda.com/academy/en/lessons/what-are-public-keys-private-keys-and-wallet-addresses/)

[Real Python - Python and REST APIs: Interacting With Web Services](https://realpython.com/api-integration-in-python)

[Django REST framework - API Guide](https://www.django-rest-framework.org/)

[Bitcoin Wiki - Deterministic wallet](https://en.bitcoin.it/wiki/Deterministic_wallet)

[Python Bitcoin Library - documentation](https://bitcoinlib.readthedocs.io/en/latest/)

[Ethereum for Python Developers](https://ethereum.org/en/developers/docs/programming-languages/python/)
