import aocd
import os
from unittest import TestCase

from aoc2024.day_solutions.day03 import parse_input, sum_num_lists
from aoc2024.session_cookie import AOCD_SESSION_COOKIE


class Test(TestCase):
    os.environ['AOC_SESSION'] = AOCD_SESSION_COOKIE
    corrupted_input = aocd.get_data(day=3, year=2024)

    def test_parse_input(self):
        corrupted_input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        res = parse_input(corrupted_input=corrupted_input)
        expected_res = [[2, 4], [5, 5], [11, 8], [8, 5]]
        self.assertEqual(res, expected_res)

    def test_sum_num_lists(self):
        corrupted_input = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
        res = sum_num_lists(corrupted_input=corrupted_input)
        self.assertEqual(res, 161)

    def test_sum_num_lists_full_data(self):
        res = sum_num_lists(corrupted_input=self.corrupted_input)
        self.assertEqual(res, 175015740)

    def test_sum_num_lists_conditional(self):
        corrupted_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()mul(2,3)"
        res = sum_num_lists(corrupted_input=corrupted_input, conditional=True)
        self.assertEqual(res, 48)

    def test_sum_num_lists_conditional_full_data(self):
        res = sum_num_lists(corrupted_input=self.corrupted_input,
                            conditional=True)
        self.assertEqual(res, 112272912)
