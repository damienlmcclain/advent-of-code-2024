from unittest import TestCase

from aoc2024.day01 import find_difference, find_similarity_score
from aoc2024.session_cookie import AOCD_SESSION_COOKIE
from aoc2024.utils import input_parser, split_strings


class Test(TestCase):

    def test_find_difference(self):
        list_1 = [3, 4, 2, 1, 3, 3]
        list_2 = [4, 3, 5, 3, 9, 3]

        res = find_difference(location_list_1=list_1, location_list_2=list_2)
        self.assertEqual(res, 11)

    def test_find_difference_full_data(self):
        input_data = input_parser(day=1,
                                  year=2024,
                                  session_cookie=AOCD_SESSION_COOKIE)
        list_1, list_2 = split_strings(input_data)
        res = find_difference(location_list_1=list_1, location_list_2=list_2)
        expected_res = 1197984
        self.assertEqual(res, expected_res)

    def test_find_similarity_score(self):
        list_1 = [3, 4, 2, 1, 3, 3]
        list_2 = [4, 3, 5, 3, 9, 3]

        res = find_similarity_score(location_list_1=list_1,
                                    location_list_2=list_2)
        self.assertEqual(res, 31)

    def test_find_similarity_score_full_data(self):
        input_data = input_parser(day=1,
                                  year=2024,
                                  session_cookie=AOCD_SESSION_COOKIE)
        list_1, list_2 = split_strings(input_data)

        res = find_similarity_score(location_list_1=list_1,
                                    location_list_2=list_2)
        self.assertEqual(res, 23387399)
