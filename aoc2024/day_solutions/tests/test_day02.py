from unittest import TestCase

from aoc2024.day_solutions.day02 import determine_safety
from aoc2024.session_cookie import AOCD_SESSION_COOKIE
from aoc2024.utils import input_parser


class Test(TestCase):

    def test_determine_safety(self):
        value_list = input_parser(
            filename='day_solutions/tests/fixtures/day_02_example.txt')
        safety_score = determine_safety(value_list=value_list)
        self.assertEqual(safety_score, 2)

    def test_determine_safety_full_data(self):
        value_list = input_parser(day=2,
                                  year=2024,
                                  session_cookie=AOCD_SESSION_COOKIE)
        safety_score = determine_safety(value_list=value_list)
        self.assertEqual(safety_score, 252)
