from helpers import get_input_as_dict

input_dict = get_input_as_dict('04')

def get_part_1_answer(input_dict):
    total_score = 0
    for card_set in input_dict:
        card_list = input_dict[card_set].split("|")
        winning_numbers = set(card_list[0].split(" "))
        winning_numbers.remove('')
        had_numbers = set(card_list[1].split(" "))
        had_numbers.remove('')
        matched_numbers = winning_numbers.intersection(had_numbers)
        print(matched_numbers)
        match_count = len(matched_numbers)
        print(f"found {match_count} matches")
        if match_count == 0:
            print(f"card score is 0")
            continue
        card_score = pow(2, (match_count - 1))
        print(f"card score is {card_score}")
        total_score = total_score + card_score
    return total_score

print(get_part_1_answer(input_dict))