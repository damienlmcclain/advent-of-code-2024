from typing import List


def find_difference(location_list_1: List[int],
                    location_list_2: List[int]) -> int:
    """
    Given two lists of ints, sorts them and finds the difference between each number pair
    and returns them as a list. This solves day 1, part 1 of AoC.

    Parameters
    ----------
    location_list_1
        The first list of locations as ints.
    location_list_2
        The second list of locations as ints.

    Returns
    -------
    The sum of the differences between the lists.
    """

    sorted_location_list_1 = sorted(location_list_1)
    sorted_location_list_2 = sorted(location_list_2)

    difference_sum = 0

    for list_1_num, list_2_num in zip(sorted_location_list_1,
                                      sorted_location_list_2):
        difference_sum += abs(list_2_num - list_1_num)

    return difference_sum


def find_similarity_score(location_list_1: List[int],
                          location_list_2: List[int]) -> int:
    """
    Given two lists of ints, iterates through the first list and finds how many times that number is present
    in the second list. Each int in the first list is multiplied by the number of times it appears in the second
    list. This solves day 1, part 2.

    Parameters
    ----------
    location_list_1
        The first list of locations as ints.
    location_list_2
        The second list of locations as ints.

    Returns
    -------
    The similarity score of the two lists.
    """

    similarity_score = 0
    for list_1_num in location_list_1:
        score = list_1_num * location_list_2.count(list_1_num)
        similarity_score += score

    return similarity_score
