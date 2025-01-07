from typing import List
import re


def check_substring(substring: str) -> List:
    """
    Checks the substring for numbers in an (x, y) configuration.

    Parameters
    ----------
    substring
        The substring to parse for numbers in an (x, y) configuration.

    Returns
    -------
    A list of the first number pair within the substring as ints. If none
    are found, returns an empty list.
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


def parse_input(corrupted_input: str,
                conditional: bool = False) -> List[List[int]]:
    """
    Parses the input string to find acceptable int pairs.

    Parameters
    ----------
    corrupted_input
        The string to parse.
    conditional
        True if conditionals need to be considered. False if they don't.

    Returns
    -------
    A list of lists of acceptable ints.
    """
    list_of_nums = []
    str_to_find = 'mul'
    mul_indexes = [
        i.start() for i in re.finditer(str_to_find, corrupted_input)
    ]

    if conditional is True:
        # start with 0 because mul instructions are enabled at the beginning
        do_indexes = [0]
        do_indexes.extend(
            [i.start() for i in re.finditer('do\(\)', corrupted_input)])
        dont_indexes = [
            i.start() for i in re.finditer("don\'t\(\)", corrupted_input)
        ]

        while mul_indexes:
            if not do_indexes:
                return list_of_nums
            elif not dont_indexes:
                # no more don'ts so evaluate everything remaining
                muls_to_evaluate = []
                for idx in mul_indexes:
                    if idx > do_indexes[0]:
                        muls_to_evaluate.append(idx)
                for value in muls_to_evaluate:
                    check = check_substring(corrupted_input[value +
                                                            len(str_to_find):])
                    if check:
                        list_of_nums.append(check)
                    mul_indexes = mul_indexes[1:]
                return list_of_nums
            elif do_indexes[0] > dont_indexes[0]:
                dont_indexes = dont_indexes[1:]
            elif do_indexes[0] < mul_indexes[0] < dont_indexes[0]:
                check = check_substring(
                    corrupted_input[mul_indexes[0] +
                                    len(str_to_find):dont_indexes[0]])
                if check:
                    list_of_nums.append(check)
                mul_indexes = mul_indexes[1:]
            elif do_indexes[0] < mul_indexes[0] and dont_indexes[
                    0] < mul_indexes[0]:
                do_indexes = do_indexes[1:]
            else:
                mul_indexes = mul_indexes[1:]
    else:
        for idx in mul_indexes:
            check = check_substring(corrupted_input[idx + len(str_to_find):])
            if check:
                list_of_nums.append(check)

    return list_of_nums


def sum_num_lists(corrupted_input: str, conditional: bool = False) -> int:
    """
    Parses the input list for acceptable ints. Then multiplies each sublist
    before summing them.

    Parameters
    ----------
    corrupted_input
        The input to parse.
    conditional
        True if conditionals need to be considered. False if they don't.

    Returns
    -------
    The total sum of the product of each int pair.
    """

    num_list = parse_input(corrupted_input=corrupted_input,
                           conditional=conditional)

    total_sum = 0

    for sublist in num_list:
        product = 1
        for num in sublist:
            product = product * num
        total_sum += product

    return total_sum
