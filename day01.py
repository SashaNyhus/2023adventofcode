import re
from inputs.day01 import input_list

# input_list = ["two1nine",
# "eightwothree",
# "abcone2threexyz",
# "xtwone3four",
# "4nineeightseven2",
# "zoneight234",
# "7pqrstsixteen"]

# # part one

# numbers_list = []
# for messy_str in input_list:
#     just_numbers = re.sub("\D", "", messy_str)
#     first_digit = just_numbers[0]
#     second_digit = just_numbers[-1]
#     numbers_list.append(int(f"{first_digit}{second_digit}"))

# print(sum(numbers_list))



# part two

def get_numbers_from_text(string):
    print(string)
    match_data = {
        "one": 'one1one',
        "two": 'two2two',
        "three": 'three3three',
        "four": 'four4four',
        "five": 'five5five',
        "six": 'six6six',
        "seven": 'seven7seven',
        "eight": 'eight8eight',
        "nine": 'nine9nine'
    }
    for key, value in match_data.items():
        string = re.sub(key, value, string)
    print(string)
    return string


second_numbers_list = []
for messy_str in input_list:
    messy_str = get_numbers_from_text(messy_str)
    just_numbers = re.sub("\D", "", messy_str)
    first_digit = just_numbers[0]
    second_digit = just_numbers[-1]
    new_pair = int(f"{first_digit}{second_digit}")
    print(new_pair)
    second_numbers_list.append(new_pair)
print(second_numbers_list)
print(sum(second_numbers_list))


# 53536 is wrong