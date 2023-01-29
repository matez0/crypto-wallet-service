from unittest import TestCase
from unittest.mock import patch

from bitcoinlib.keys import BKeyError

from .address_generator import generate_address, ParseError

MUT_PATH = 'wallet.address_generator'


@patch(MUT_PATH + '.HDKey')
class TestAddressGenerator(TestCase):
    INVALID_CURRENCY_MSG = 'Invalid currency'

    def test_error_when_currency_is_not_supported(self, hd_key):
        with self.assertRaises(ParseError) as error:
            generate_address('USD', 'private-key', index=3)

        self.assertIn(self.INVALID_CURRENCY_MSG, str(error.exception))

        hd_key.assert_not_called()

    def test_error_when_private_key_is_not_valid(self, hd_key):
        hd_key.side_effect = BKeyError()
        private_key = 'private-key'

        with self.assertRaises(ParseError) as error:
            generate_address('BTC', private_key, index=3)

        self.assertNotIn(self.INVALID_CURRENCY_MSG, str(error.exception))

        hd_key.assert_called_once_with(private_key)

    def test_generating_address_is_successful(self, hd_key):
        private_key = 'private-key'
        index = 123

        self.assertEqual(
            generate_address('BTC', private_key, index),
            hd_key.return_value.child_private.return_value.address.return_value
        )

        hd_key.assert_called_once_with(private_key)
        hd_key.return_value.child_private.assert_called_once_with(index)
