from unittest import TestCase
import GiftExchange


class GiftExchangeTests(TestCase):

    def test_validate_input(self):
        """ Checks the input of a name to verify alpha characters are entered and duplicates aren't present. """
        name1 = "marc andre"
        name2 = "9"
        GiftExchange.validate_input(name1)
        self.assertNotIn(name1, GiftExchange.participant_list)
        result = GiftExchange.validate_input("9")
        self.assertNotIn(result, GiftExchange.participant_list)
        GiftExchange.participant_list = ['Jordan']
        result = GiftExchange.validate_input('jordan')
        self.assertEqual(result, len(GiftExchange.participant_list) == 1)
        result = GiftExchange.validate_input('mateusz')
        self.assertIn(result, GiftExchange.participant_list)
