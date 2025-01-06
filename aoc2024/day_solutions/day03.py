from typing import List
import re


def check_char(input_str):
    nums = list(range(10))
    num_str_list = [str(x) for x in nums]
    print(f'input_str {input_str}')
    first_mul = input_str.count('mul')
    print(f'first_mul {first_mul}')
    num_counted = 0
    num_list = []
    num = ''

    for char in input_str[first_mul:]:
        if num:
            print(f'num {num}')
        print(f'char {char}')
        if len(num_list) == 2:
            return num_list

        # print(char == ',')
        # print(f'is numb True: {num is True}')

        if char == '(':
            continue

        if char in num_str_list:
            num += char
            print(f'num after char addition {num}')
            print(f'num {num}')
            print(len(num) != 0)
            # if num is True:
            #     print('num is True')
        elif char == ',' and len(num) != 0:
            print('passed len test')
            num_list.append(int(num))
            print(num_list)
            num = ''
        elif char == ')' and len(num) != 0:
            num_list.append(int(num))
            return num_list

    return num_list


def parse_input(corrupted_input: str) -> List[List[int]]:
    list_of_nums = []
    str_to_find = 'mul'
    # mul_indexes = re.findall(str_to_find, corrupted_input)
    mul_indexes = [i.start() for i in re.findall(str_to_find, corrupted_input)]
    print(mul_indexes)
    for idx in range(len(corrupted_input)):
        print(f'corrupted_input[idx]: {corrupted_input[idx]}')
        check = check_char(corrupted_input[idx:])
        print(f'check {check}')
        if check:
            list_of_nums.append(check)

    print(list_of_nums)
    return list_of_nums


# def parse_input(corrupted_input: str) -> List[List[int]]:
#     str_to_find = 'mul('
#     mul_count = corrupted_input.count(str_to_find)
#     nums = list(range(10))
#     num_str_list = [str(x) for x in nums]
#     num_list = []
#     mul_index_offset = 0
#     for i in range(mul_count):
#         current_num = ''
#         current_num_list = []
#         print(corrupted_input[i * 4:])
#         print(corrupted_input[i * 4:].find(str_to_find))
#         mul_index = corrupted_input[i * 4:].find(str_to_find)
#         for char in corrupted_input[mul_index:]:
#             if char in num_str_list:
#                 current_num += char
#             elif char == ',' and current_num:
#                 current_num_list.append(int(current_num))
#                 current_num = ''
#             elif char == ')' and current_num:
#                 current_num_list.append(int(current_num))
#                 num_list.append(current_num_list)
#                 # for num in current_num_list:
#                 #     mul_index_offset += num
#                 # print(mul_index_offset)
#                 break
#
#
#     return num_list



# def parse_input(corrupted_input: str) -> List[List[int]]:
#     """
#
#     Parameters
#     ----------
#     corrupted_input
#
#     Returns
#     -------
#
#     """
#
#     nums_to_multiply = []
#     nums = list(range(10))
#     num_str_list = [str(x) for x in nums]
#     print(num_str_list)
#
#     # mul_index = corrupted_input.find('mul(') + 4
#     # print(f'mul_index: {mul_index}')
#     current_nums = []
#     current_num = ''
#     current_str = ''
#     str_to_find = 'mul('
#     str_dict = {0: 'm', 1: 'u', 2: 'l', 3: '('}
#     str_dict = {'m': 0, 'u': 1, 'l': 2, '(': 3}
#     for idx, char in enumerate(corrupted_input):
#         if current_str == str_to_find:
#             print('found str to find')
#             if char == ')':
#                 if current_num:
#                     print(f'current_num: {current_num}')
#                     num = int(current_num)
#                     current_nums.append(num)
#                     nums_to_multiply.append(current_nums)
#                     print(f'extending {current_nums} to nums to multiply')
#                 current_num = ''
#                 current_nums = []
#                 current_str = ''
#                 continue
#             elif char == '(':
#                 current_str = ''
#             elif char in num_str_list:
#                 current_num += char
#                 print(f'adding {char} to {current_num}')
#             elif char == ',' and current_num:
#                 print(f'type current num: {type(current_num)}')
#                 num = int(current_num)
#                 current_nums.append(num)
#                 print(f'current num {current_num} before reset due to ,')
#                 current_num = ''
#                 # continue
#             else:
#                 print(f'{char} not in char list')
#                 current_num = ''
#                 current_str = ''
#                 current_nums = []
#                 print(f'reset current num to {current_num}')
#                 print(f'resetting current str')
#         elif char in str_to_find:
#             print(current_str[idx:].find(char) + 1)
#             print(int(str_dict[char]))
#             if current_str[idx:].find(char) == str_dict[char]:
#                 current_str += char
#                 print(current_str)
#             else:
#                 current_str = ''
#         else:
#             print(f'{char} not in char list')
#             current_num = ''
#             current_str = ''
#             current_nums = []
#             print(f'reset current num to {current_num}')
#             print(f'resetting current str')
#
#     return nums_to_multiply

# def parse_input(corrupted_input: str) -> List[List[int]]:
#     str_to_find = 'mul('
#     nums = list(range(10))
#     num_str_list = [str(x) for x in nums]
#     all_nums = []
#     nums_to_add = []
#     num = ''
#     idx = 0
#     current_str = ''
#     while idx <= len(corrupted_input) - 1:
#         print(corrupted_input[idx])
#         if current_str == str_to_find:
#             if corrupted_input[idx] in num_str_list:
#                 num += corrupted_input[idx]
#                 idx += 1
#             elif corrupted_input[idx] == ',' and num:
#                 nums.append(int(num))
#                 idx += 1
#                 num = ''
#             elif corrupted_input[idx] == ')' and num:
#                 nums_to_add.append(num)
#                 num = ''
#                 all_nums.extend(nums)
#                 print(corrupted_input)
#                 idx = 0
#         else:
#             print(idx % 4)
#             if idx % 4 == str_to_find[idx]:
#                 current_str += corrupted_input[idx]
#                 print(current_str)
#                 idx += 1
#             else:
#                 current_str = ''
#                 idx = 0
#         # idx += 1
#
#     print(all_nums)
#     return(all_nums)

def sum_num_lists(corrupted_input: str) -> int:
    """

    Parameters
    ----------
    corrupted_input

    Returns
    -------

    """

    num_list = parse_input(corrupted_input=corrupted_input)

    total_sum = 0

    for sublist in num_list:
        product = 1
        for num in sublist:
            product = product * num
        total_sum += product

    print(total_sum)

    return total_sum
