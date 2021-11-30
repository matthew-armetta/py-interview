from unittest import TestCase
import CodeChallenges


class QuestionsTestCases(TestCase):

    # tests the sum of two numbers
    def test_add_numbers(self):
        result = CodeChallenges.add_numbers(44, 99)
        self.assertEqual(result, 143)

    # tests the reversal of a given string
    def test_reverse_string(self):
        result = CodeChallenges.reverse_string("I'm a hot dog")
        self.assertEqual(result, "god toh a m'I")

    # tests the comparison of two lists
    def test_find_missing(self):
        sample_list = [1, 2, 3, 4, 5]
        sample_partial_list = [2, 3, 5]
        result = CodeChallenges.find_missing(sample_list, sample_partial_list)
        self.assertEqual(result, [1, 4], 'The function found the missing values.')
