from operator import index
from helpers import get_input_as_list

input_list = get_input_as_list('03')
# print(input_list)



def find_numbers_in_row(row):
    numbers_found = []
    working_number = ""
    working_index_start = None
    for element_index in range(0, len(row)):
        element = row[element_index]
        if element.isnumeric():
            working_number = working_number + element
            if working_index_start is None:
                working_index_start = element_index
        elif len(working_number) > 0:
            numbers_found.append({
                'number_value': int(working_number),
                'index_start': working_index_start,
                'index_end': element_index - 1
            })
            working_number = ""
            working_index_start = None
    # the above code doesn't work for numbers at the end of the line, since it relies on finding a character that's not a number to recognize that a number has ended.
    # So before we move on, check to see if we still have working number data
    if len(working_number) > 0:
        numbers_found.append({
            'number_value': int(working_number),
            'index_start': working_index_start,
            'index_end': len(row) - 1
            })
    return numbers_found

def is_symbol(character):
    if character.isnumeric():
        return False
    elif character == '.':
        return False
    else:
        # print(f'{character} is a symbol')
        return True

def check_if_part_number(number_data, row, row_above, row_below):
    # set up locations to check
    index_start = number_data['index_start']
    if index_start != 0:
        index_start = index_start - 1
    index_end = number_data['index_end']
    if index_end != (len(row) - 1):
        index_end = index_end + 1

    # check for symbols
    if is_symbol(row[index_start]):
        print(f"{number_data['number_value']} with symbol in row")
        return True
    elif is_symbol(row[index_end]):
        print(f"{number_data['number_value']} with symbol in row")
        return True
    for test_index in range(index_start, (index_end + 1)):
        # print(test_index)
        if is_symbol(row_above[test_index]) or is_symbol(row_below[test_index]):
            print(number_data['number_value'])
            return True
    else:
        return False


input_rows_len = len(input_list)
current_sum = 0
rejected_numbers = []
part_numbers = []

for row_index in range(0, (input_rows_len)):
    print(f'checking row {row_index}')
    if row_index == 24:
        print('break here')
    if row_index == 0:
        row_above = ['.'] * input_rows_len
    else:
        row_above = input_list[row_index - 1]
    current_row = input_list[row_index]
    if row_index == (len(input_list) - 1):
        row_below = ['.'] * input_rows_len
    else:
        row_below = input_list[row_index + 1]
    numbers_found = find_numbers_in_row(current_row)
    print(f"{len(numbers_found)} numbers found")
    for number_data in numbers_found:
        is_part_number = check_if_part_number(number_data, current_row, row_above, row_below)
        if is_part_number:
            part_numbers.append(number_data['number_value'])
            current_sum = current_sum + number_data['number_value']
            print(row_index)
            print(number_data)
        else:
            rejected_numbers.append(number_data['number_value'])
    # print(numbers_found)
print(current_sum)
rejected_numbers.sort()
print(len(rejected_numbers))
print(rejected_numbers)
# print(len(part_numbers))
# print(part_numbers)


# 518337 is too low 
# 569473 is too high 
# 518219 is too low 