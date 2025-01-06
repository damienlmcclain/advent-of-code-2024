from typing import List
import re


def check_substring(substring: str) -> List:
    """

    Parameters
    ----------
    substring
        The substring to parse for numbers in an (x, y) configuration.

    Returns
    -------
    A list of the first number pair within the substring.
    """
    nums = list(range(10))
    num_str_list = [str(x) for x in nums]
    num_list = []
    num = ''

    for idx, char in enumerate(substring):
        if idx == 0 and char == '(':
            continue

        if char in num_str_list:
            num += char
        elif char == ',' and len(num) != 0:
            num_list.append(int(num))
            num = ''
        elif char == ')' and len(num) != 0:
            num_list.append(int(num))
            return num_list
        else:
            return []

    return num_list


def parse_input(corrupted_input: str) -> List[List[int]]:
    """
    Parses the input string to find acceptable int pairs.

    Parameters
    ----------
    corrupted_input
        The string to parse.

    Returns
    -------
    A list of lists of acceptable ints.
    """
    list_of_nums = []
    str_to_find = 'mul'
    mul_indexes = [
        i.start() for i in re.finditer(str_to_find, corrupted_input)
    ]

    for idx in mul_indexes:
        check = check_substring(corrupted_input[idx + 3:])
        if check:
            list_of_nums.append(check)

    return list_of_nums


def sum_num_lists(corrupted_input: str) -> int:
    """
    Parses the input list for acceptable ints. Then multiplies each sublist
    before summing them.

    Parameters
    ----------
    corrupted_input
        The input to parse.

    Returns
    -------
    The total sum of the product of each int pair.
    """

    num_list = parse_input(corrupted_input=corrupted_input)

    total_sum = 0

    for sublist in num_list:
        product = 1
        for num in sublist:
            product = product * num
        total_sum += product

    return total_sum
