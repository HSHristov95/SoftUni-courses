deck_of_cars = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    middle_index = len(deck_of_cars) // 2

    left_half = deck_of_cars[:middle_index]
    right_half = deck_of_cars[middle_index:]

    new_deck_of_cards = []

    for card_index in range(len(left_half)):
        new_deck_of_cards.append(left_half[card_index])
        new_deck_of_cards.append(right_half[card_index])

    deck_of_cars = new_deck_of_cards.copy()

print(deck_of_cars)