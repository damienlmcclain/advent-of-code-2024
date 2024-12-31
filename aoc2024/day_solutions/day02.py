from typing import List, Tuple
#
#
# def determine_safety(value_list: List[str], dampener: bool = False) -> int:
#     """
#     Per day 2 of AoC, determines if reports are overall_safe and returns the total
#     number of overall_safe reports.
#
#     Parameters
#     ----------
#     value_list
#         The list of values to evaluate as str.
#     dampener
#         Whether to enable the dampener or not. If removing a single level
#         from an unsafe report makes it overall_safe, it will count as overall_safe.
#
#     Returns
#     -------
#     The number of overall_safe reports.
#     """
#
#     safety_score = 0
#     for values in value_list[:7]:
#         safe = True
#         last_num = None
#         increasing = True
#         decreasing = True
#         overall_increasing = []
#         overall_decreasing = []
#         numbers_within_range = []
#         num_unsafe_levels = 0
#         nums_skipped = 0
#         repeated_nums = []
#         is_consistent = []
#
#         values = values.split(' ')
#         print(values)
#         for value in values:
#
#             print(f'last num: {last_num}, current num: {value}')
#
#             if dampener is True:
#                 safe = True
#                 increasing = True
#                 decreasing = True
#
#             # if it's the first number, it doesn't need to be checked
#             if not last_num:
#                 last_num = value
#                 continue
#             elif values.count(value) > 1 and value not in repeated_nums:
#                 nums_skipped += 1
#                 repeated_nums.append(value)
#                 # last_num = value
#             else:
#                 value_difference = int(value) - int(last_num)
#                 if value_difference > 0:
#                     decreasing = False
#                     increasing = True
#                     overall_decreasing.append(False)
#                     overall_increasing.append(True)
#                 elif value_difference < 0:
#                     increasing = False
#                     decreasing = True
#                     overall_increasing.append(False)
#                     overall_decreasing.append(True)
#                 elif value_difference == 0:
#                     nums_skipped += 1
#                     numbers_within_range.append(False)
#                     # break
#
#                 # if increasing is False and decreasing is False and dampener is False:
#                 #     num_unsafe_levels += 1
#                 #     safe = False
#                 #     break
#
#                 value_difference = int(value) - int(last_num)
#                 if abs(value_difference) not in [1, 2, 3]:
#                     # print(last_num, value)
#                     numbers_within_range.append(False)
#                     print(f'value_difference: {value_difference}')
#                     if not dampener:
#                         num_unsafe_levels += 1
#                         safe = False
#                         # last_num = value
#                     nums_skipped += 1
#                     # last_num = value
#                 else:
#                     numbers_within_range.append(True)
#                     last_num = value
#             print(f'nums_skipped: {nums_skipped}')
#             if dampener is True:
#                 is_consistent = []
#                 # if 2 or more numbers are skipped, the report automatically fails
#                 print(nums_skipped)
#                 print(f'overall_increasing: {overall_increasing}')
#                 print(f'overall_decreasing: {overall_decreasing}')
#                 print(f'overall_increasing.count(False): {overall_increasing.count(False)}')
#                 print(
#                     f'overall_increasing.count(True): {overall_increasing.count(True)}'
#                     )
#                 overall_increasing_false_count = overall_increasing.count(False)
#                 overall_increasing_true_count = overall_increasing.count(True)
#                 overall_decreasing_false_count = overall_decreasing.count(False)
#                 overall_decreasing_true_count = overall_decreasing.count(True)
#                 # print(f'len(values): {len(values)}')
#                 # if nums_skipped + numbers_within_range.count(False) <= 1:
#                 #     safety_score += 1
#                 #     print(f'fewer than 2 nums_skipped. increasing')
#
#         print(f'numbers_within_range: {numbers_within_range}')
#         if dampener is True:
#             consistent = True
#
#             if overall_increasing_false_count > 1 and overall_increasing_true_count >= len(values) - 2:
#                 consistent = False
#             elif overall_increasing_true_count > 1 and overall_increasing_false_count >= len(values) - 2:
#                 consistent = False
#
#             num_safe = 0
#             print(f'numbers_within_range: {numbers_within_range}')
#             print(f'consistent: {consistent}')
#             for num_range in numbers_within_range:
#                 if num_range is True and consistent is True:
#                     print(f'safe because no bad nums and consistent is True')
#                     num_safe += 1
#                 else:
#                     print(num_range)
#                     print(f'not safe because bad nums or consistent is False')
#                 # if overall_increasing.count(False) < 2 or overall_increasing.count(True) < 2:
#                 #     print('increasing: more than 1 False and 1 True')
#                 #     safety_score += 1
#                 # elif overall_decreasing.count(False) < 2 or overall_decreasing.count(True) < 2:
#                 #     safety_score += 1
#                 #     print('decreasing: more than 1 False and 1 True')
#                 # elif nums_skipped <= 1:
#                 #     safety_score += 1
#                 # num_unsafe_levels = 0
#                 # for increase, decrease, safety in zip(overall_increasing, overall_decreasing, numbers_within_range):
#                 #     print(increase, decrease, safety)
#                 #
#                 # if not all(overall_increasing) or not all(overall_decreasing):
#                 #     num_unsafe_levels += 1
#                 # if more than 1 is False, it fails the safety check
#
#                 # print(f'num_unsafe_levels: {num_unsafe_levels}')
#             print(f'num_safe: {num_safe}')
#             print(f'len values - 1 - len(repeated_nums): {len(values) - 1 - len(repeated_nums)}')
#             if num_safe >= len(values) - 1 - len(repeated_nums):
#                 print(f'increasing safety score')
#                 safety_score += 1
#         else:
#             if safe is True:
#                 safety_score += 1
#         print(f'safety_score: {safety_score}')
#     print(' ')
#
#     return safety_score

from typing import Dict, List


def determine_safety(value_list: List[str]) -> Tuple[int, List[List[Dict]]]:
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
    A list of lists of dicts for each report.
    """

    safety_score = 0
    list_of_pass_fail = []
    for values in value_list:
        print(values)
        safe = True
        last_num = None
        increasing = True
        decreasing = True
        values = values.split(' ')
        pass_fail = []

        for idx, value in enumerate(values):
            print(last_num, value)
            pass_fail_value = {'idx': idx}
            # if it's the first number, it doesn't need to be checked
            if not last_num:
                last_num = value
                continue
            else:
                value_difference = int(value) - int(last_num)
                if value_difference > 0:
                    decreasing = False
                    pass_fail_value['increasing'] = True
                elif value_difference < 0:
                    increasing = False
                    pass_fail_value['increasing'] = False

                if increasing is False and decreasing is False:
                    safe = False

                if abs(value_difference) not in [1, 2, 3]:
                    safe = False
                    pass_fail_value['passing_difference'] = False
                else:
                    pass_fail_value['passing_difference'] = True
            last_num = value
            print(f'pass_fail_value: {pass_fail_value}')
            pass_fail.extend([pass_fail_value])

        if safe is True:
            safety_score += 1
        list_of_pass_fail.append(pass_fail)
    print(list_of_pass_fail)

    return safety_score, list_of_pass_fail


def use_dampener(list_of_pass_fail: List[List[Dict]]) -> int:
    """
    Evaluates the information from determine_safety.

    Parameters
    ----------
    list_of_pass_fail
        The list of passing and failing from determine_safety.
        Each list is the total, each sublist is a report, and each dict is a
        level.

    Returns
    -------
    The number of reports that pass the safety requirements.
    """

    for report in list_of_pass_fail:
        