from unittest import TestCase

from aoc2024.day_solutions.day02 import tally_up_score
from aoc2024.session_cookie import AOCD_SESSION_COOKIE
from aoc2024.utils import input_parser


class Test(TestCase):

    def test_determine_safety(self):
        reports = input_parser(
            filename='day_solutions/tests/fixtures/day_02_example.txt')
        safety_score = tally_up_score(reports=reports)
        self.assertEqual(safety_score, 2)

    def test_determine_safety_full_data(self):
        reports = input_parser(day=2,
                               year=2024,
                               session_cookie=AOCD_SESSION_COOKIE)
        safety_score = tally_up_score(reports=reports)
        self.assertEqual(safety_score, 252)

    def test_determine_safety_with_dampener(self):
        reports = input_parser(
            filename='day_solutions/tests/fixtures/day_02_example.txt')
        safety_score = tally_up_score(reports=reports, dampener=True)
        self.assertEqual(safety_score, 4)

    def test_determine_safety_with_dampener_full_data(self):
        reports = input_parser(day=2,
                               year=2024,
                               session_cookie=AOCD_SESSION_COOKIE)
        safety_score = tally_up_score(reports=reports, dampener=True)
        self.assertEqual(safety_score, 324)
