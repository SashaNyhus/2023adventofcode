from helpers import get_input_as_dict

input_dict = get_input_as_dict('02')
print(input_dict)
cleaned_input = {}
for game_key, game_data in input_dict.items():
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
    cleaned_input[game_key] = reformatted_draws
print(cleaned_input)