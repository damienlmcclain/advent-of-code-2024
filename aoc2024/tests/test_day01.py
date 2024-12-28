from unittest import TestCase

from aoc2024.day01 import find_difference


class Test(TestCase):

    def test_find_difference(self):
        list_1 = [3, 4, 2, 1, 3, 3]
        list_2 = [4, 3, 5, 3, 9, 3]

        res = find_difference(location_list_1=list_1, location_list_2=list_2)
        expected_res = 11

        self.assertEqual(res, expected_res)

