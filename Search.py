n = int(input())
special_word = input()

unfiltered_list = []

for _ in range(n):
    strings = input()
    unfiltered_list.append(strings)

filtered_list = []

for strs in unfiltered_list:
    if special_word in strs:
        filtered_list.append(strs)

print(unfiltered_list)
print(filtered_list)