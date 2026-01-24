beggars_take = input().split(', ')
number_of_beggars = int(input())
beggars_take_as_int = []

for money in beggars_take:
    beggars_take_as_int.append(int(money))

beggars_sum = []
start_index = 0

for beggars in range(number_of_beggars):
    current_beggar_sum = 0
    for index in range(start_index, len(beggars_take_as_int), number_of_beggars):
        current_beggar_sum += beggars_take_as_int[index]

    beggars_sum.append(current_beggar_sum)
    start_index += 1

print(beggars_sum)