from unittest import TestCase
import GiftExchange


class GiftExchangeTests(TestCase):

    def test_validation(self):
        """ Checks the input of a name to verify alpha characters are entered and duplicates aren't present. """
        result = GiftExchange.validate_input("marc andre")
        self.assertEqual(result, False)
        result = GiftExchange.validate_input("9")
        self.assertEqual(result, False)
        GiftExchange.participant_list = ['Jordan']
        result = GiftExchange.validate_input('jordan')
        self.assertEqual(result, False)
        result = GiftExchange.validate_input('mateusz')
        self.assertEqual(result, True)

