from typing import List


def determine_safety(value_list: List[str]) -> int:
    """
    Per day 2 of AoC, determines if reports are safe and returns the total
    number of safe reports.

    Parameters
    ----------
    value_list
        The list of values to evaluate as str.

    Returns
    -------
    The number of safe reports.
    """

    safety_score = 0
    for values in value_list:
        safe = True
        last_num = None
        increasing = True
        decreasing = True
        values = values.split(' ')

        for value in values:
            if value == ' ':
                continue

            # if it's the first number, it doesn't need to be checked
            if not last_num:
                last_num = value
            else:
                value_difference = int(value) - int(last_num)
                if value_difference > 0:
                    decreasing = False
                elif value_difference < 0:
                    increasing = False

                if increasing is False and decreasing is False:
                    safe = False
                    break

                if abs(value_difference) not in [1, 2, 3]:
                    safe = False
                    break
                else:
                    last_num = value

        if safe is True:
            safety_score += 1

    return safety_score
