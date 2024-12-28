from unittest import TestCase

from aoc2024.utils import convert_str_to_int, input_parser


class Test(TestCase):

    def test_input_parser(self):
        res = input_parser(
            filename='aoc2024/tests/fixtures/day_01_list_1.txt')
        expected_res = ['3', '4', '2', '1', '3', '3']
        self.assertEqual(res, expected_res)

    def test_convert_str_to_int(self):
        str_list = ['3', '4', '2', '1', '3', '3']
        res = convert_str_to_int(str_list)
        expected_res = [3, 4, 2, 1, 3, 3]
        self.assertEqual(res, expected_res)
