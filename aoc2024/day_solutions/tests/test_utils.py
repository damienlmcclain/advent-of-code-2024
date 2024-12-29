from unittest import TestCase

from aoc2024.utils import convert_str_to_int, input_parser, split_strings


class Test(TestCase):

    def test_input_parser(self):
        res = input_parser(
            filename='day_solutions/tests/fixtures/day_01_list_1.txt')
        expected_res = ['3', '4', '2', '1', '3', '3']
        self.assertEqual(res, expected_res)

        res = input_parser(
            filename='day_solutions/tests/fixtures/day_02_example.txt')
        expected_res = ['7 6 4 2 1', '1 2 7 8 9', '9 7 6 2 1', '1 3 2 4 5', '8 6 4 4 1', '1 3 6 7 9']
        self.assertEqual(res, expected_res)

    def test_convert_str_to_int(self):
        str_list = ['3', '4', '2', '1', '3', '3']
        res = convert_str_to_int(str_list=str_list)
        expected_res = [3, 4, 2, 1, 3, 3]
        self.assertEqual(res, expected_res)

    def test_split_strings(self):
        example_str_list = ['77710   11556', '22632   23674', '82229   77288']
        res = split_strings(str_list=example_str_list, num_spaces=3)
        expected_res = ([77710, 22632, 82229], [11556, 23674, 77288])
        self.assertEqual(res, expected_res)
