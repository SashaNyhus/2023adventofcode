from cProfile import run
from helpers import get_input_as_dict

# format input
input_dict = get_input_as_dict('02')
print(input_dict)
cleaned_input = {}
for game_key, game_data in input_dict.items():
    game_key_int = game_key.split(' ')[1]
    split_games = game_data.split(';')
    reformatted_draws = []
    for draw in split_games:
        draw_list = draw.split(',')
        draw_data = {}
        for result in draw_list:
            result_data = result.split(' ')
            print(result_data)
            draw_data[result_data[2]]  = result_data[1]
            print(draw_data)
        reformatted_draws.append(draw_data)
        # print(draw)
    cleaned_input[game_key_int] = reformatted_draws
print(cleaned_input)

# part 1: check for valid games
color_totals = {
    'red': 12,
    'green': 13,
    'blue': 14
}

running_total = 0
for game_key, game_data in cleaned_input.items():
    valid_game = True
    for draw in game_data:
        for color, amount in draw.items():
            if color_totals[color] < int(amount):
                valid_game = False
                print(f'Game {game_key} is invalid because of {color}')
                break
        if valid_game == False:
            break
    if valid_game:
        running_total = running_total + int(game_key)
print(running_total)


# part 2 fewest possible cubes:
power_total = 0
for game_key, game_data in cleaned_input.items():
    color_counts = {
        'blue': None,
        'red': None,
        'green': None
    }
    for draw in game_data:
        for color, amount in draw.items():
            amount = int(amount)
            if ((color_counts[color] is None) or color_counts[color] < amount):
                color_counts[color] = amount
    game_power = 1
    print(color_counts)
    for color_name, color_amount in color_counts.items():
        if color_amount is not None:
            game_power = game_power * color_amount
    power_total = power_total + game_power
print(power_total)
