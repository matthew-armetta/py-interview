from unittest import TestCase
import GiftExchange


class GiftExchangeTests(TestCase):

    def test_validation(self):
        """ Checks the input of a name to verify alpha characters are entered """
        result = GiftExchange.validate_input("marc andre")
        self.assert
