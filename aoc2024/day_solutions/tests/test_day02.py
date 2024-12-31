from unittest import TestCase

from aoc2024.day_solutions.day02 import determine_safety
from aoc2024.session_cookie import AOCD_SESSION_COOKIE
from aoc2024.utils import input_parser


class Test(TestCase):

    def test_determine_safety(self):
        value_list = input_parser(
            filename='day_solutions/tests/fixtures/day_02_example.txt'
        )
        safety_score, list_of_pass_fail = determine_safety(value_list=value_list)
        self.assertEqual(safety_score, 2)
        expected_list_of_pass_fail = [[{'idx': 1, 'increasing': False, 'passing_difference': True}, {'idx': 2, 'increasing': False, 'passing_difference': True}, {'idx': 3, 'increasing': False, 'passing_difference': True}, {'idx': 4, 'increasing': False, 'passing_difference': True}], [{'idx': 1, 'increasing': True, 'passing_difference': True}, {'idx': 2, 'increasing': True, 'passing_difference': False}, {'idx': 3, 'increasing': True, 'passing_difference': True}, {'idx': 4, 'increasing': True, 'passing_difference': True}], [{'idx': 1, 'increasing': False, 'passing_difference': True}, {'idx': 2, 'increasing': False, 'passing_difference': True}, {'idx': 3, 'increasing': False, 'passing_difference': False}, {'idx': 4, 'increasing': False, 'passing_difference': True}], [{'idx': 1, 'increasing': True, 'passing_difference': True}, {'idx': 2, 'increasing': False, 'passing_difference': True}, {'idx': 3, 'increasing': True, 'passing_difference': True}, {'idx': 4, 'increasing': True, 'passing_difference': True}], [{'idx': 1, 'increasing': False, 'passing_difference': True}, {'idx': 2, 'increasing': False, 'passing_difference': True}, {'idx': 3, 'passing_difference': False}, {'idx': 4, 'increasing': False, 'passing_difference': True}], [{'idx': 1, 'increasing': True, 'passing_difference': True}, {'idx': 2, 'increasing': True, 'passing_difference': True}, {'idx': 3, 'increasing': True, 'passing_difference': True}, {'idx': 4, 'increasing': True, 'passing_difference': True}]]
        self.assertEqual(list_of_pass_fail, expected_list_of_pass_fail)
    #
    # def test_determine_safety_full_data(self):
    #     value_list = input_parser(
    #         day=2,
    #         year=2024,
    #         session_cookie=AOCD_SESSION_COOKIE
    #         )
    #     safety_score = determine_safety(value_list=value_list)
    #     self.assertEqual(safety_score, 252)
    #
    # def test_determine_safety_with_dampener(self):
    #     value_list = input_parser(
    #         filename='day_solutions/tests/fixtures/day_02_example.txt'
    #     )
    #     safety_score = determine_safety(value_list=value_list, dampener=True)
    #     self.assertEqual(safety_score, 4)
    #     self.assertEqual(1, 2)
    # #
    # # # 363 too high
    # #
    # def test_determine_safety_with_dampener_full_data(self):
    #     value_list = input_parser(
    #         day=2,
    #         year=2024,
    #         session_cookie=AOCD_SESSION_COOKIE
    #         )
    #     safety_score = determine_safety(value_list=value_list, dampener=True)
    #     self.assertEqual(safety_score, 252)
