def get_input_as_list(day_key):
    new_input = []
    with open(f'inputs/day{day_key}.txt', 'r') as file:
        for line in file:
            new_input.append(line.strip('\n'))
    file.close()
    return new_input

def get_input_as_dict(day_key):
    new_dict = {}
    list_input = get_input_as_list(day_key)
    for line in list_input:
        split_line = line.split(":")
        new_dict[split_line[0]] = split_line[1]
    return new_dict