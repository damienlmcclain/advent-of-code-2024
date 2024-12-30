from typing import List


def determine_safety(value_list: List[str], dampener: [bool] = False) -> int:
    """
    Per day 2 of AoC, determines if reports are overall_safe and returns the total
    number of overall_safe reports.

    Parameters
    ----------
    value_list
        The list of values to evaluate as str.
    dampener
        Whether to enable the dampener or not. If removing a single level
        from an unsafe report makes it overall_safe, it will count as overall_safe.

    Returns
    -------
    The number of overall_safe reports.
    """

    safety_score = 0
    for values in value_list[:4]:
        safe = True
        last_num = None
        increasing = True
        decreasing = True
        overall_increasing = []
        overall_decreasing = []
        numbers_within_range = []
        num_unsafe_levels = 0

        values = values.split(' ')
        print(values)
        for value in values:
            if value == ' ':
                continue

            if dampener is True:
                safe = True
                increasing = True
                decreasing = True

            # if it's the first number, it doesn't need to be checked
            if not last_num:
                last_num = value
            else:
                value_difference = int(value) - int(last_num)
                if value_difference > 0:
                    decreasing = False
                    overall_decreasing.append(False)
                elif value_difference < 0:
                    increasing = False
                    overall_increasing.append(False)

                if increasing is False and decreasing is False:
                    num_unsafe_levels += 1
                    safe = False

                if abs(value_difference) not in [1, 2, 3]:
                    print(last_num, value)
                    numbers_within_range.append(False)
                    if not dampener:
                        num_unsafe_levels += 1
                        safe = False
                else:
                    numbers_within_range.append(True)
                    last_num = value

        print(overall_safe)

        if dampener is True:
            num_unsafe_levels = 0
            for increase, decrease, safety in zip(overall_increasing, overall_decreasing, numbers_within_range):
                print(increase, decrease, safety)

            if not all(overall_increasing) or not all(overall_decreasing):
                num_unsafe_levels += 1
            # if more than 1 is False, it fails the safety check

            print(f'num_unsafe_levels: {num_unsafe_levels}')

        else:
            if safe is True:
                safety_score += 1
        print(safety_score)

    return safety_score
