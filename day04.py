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

# print(get_part_1_answer(input_dict))

def get_card_matches(card_list):
    winning_numbers = set(card_list[0].split(" "))
    winning_numbers.remove('')
    had_numbers = set(card_list[1].split(" "))
    had_numbers.remove('')
    matched_numbers = winning_numbers.intersection(had_numbers)
    match_count = len(matched_numbers)
    return match_count


def get_part_2_answer(input_dict):
    total_cards = 0
    copies_by_card = {i: 1 for i in range(1, (len(input_dict) + 1))}
    print(copies_by_card)
    for card_set in input_dict:
        card_id = int(card_set.strip("Card "))
        copies_of_this_card = copies_by_card[card_id]
        total_cards = total_cards + copies_of_this_card

        card_list = input_dict[card_set].split("|")
        card_matches = get_card_matches(card_list=card_list)
        print(card_matches)
        next_card = card_id + 1
        while card_matches > 0:
            copies_by_card[next_card] += copies_of_this_card
            card_matches = card_matches - 1
            next_card += 1
        print(copies_by_card)
    return total_cards

print(get_part_2_answer(input_dict))