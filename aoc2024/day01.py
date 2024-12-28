from aocd import get_data
# import os


def find_difference(location_list_1: list, location_list_2: list) -> int:
    """
    Given two lists, sorts them and finds the difference between each number pair
    and returns them as a list.

    Parameters
    ----------
    location_list_1
        The first list of locations as integers.
    location_list_2
        The second list of locations as integers.

    Returns
    -------
    The sum of the differences between the lists.
    """
    get_data(day=1, year=2024)
    sorted_location_list_1 = sorted(location_list_1)
    sorted_location_list_2 = sorted(location_list_2)

    difference_sum = 0

    for list_1_num, list_2_num in zip(sorted_location_list_1, sorted_location_list_2):
        difference_sum += abs(list_2_num - list_1_num)

    return difference_sum


