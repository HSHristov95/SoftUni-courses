n = int(input())

unfiltered_list = []

for _ in range(n):
    num = int(input())
    unfiltered_list.append(num)

command = input()
filtered_list = []

if command == 'even':
    for nums in unfiltered_list:
        if nums % 2 == 0:
            filtered_list.append(nums)
elif command == 'odd':
    for nums in unfiltered_list:
        if nums % 2 != 0:
            filtered_list.append(nums)
elif command == 'negative':
    for nums in unfiltered_list:
        if nums < 0:
            filtered_list.append(nums)
elif command == 'positive':
    for nums in unfiltered_list:
        if nums >= 0:
            filtered_list.append(nums)

print(filtered_list)