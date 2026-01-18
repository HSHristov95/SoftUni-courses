number_of_lines = int(input())

for _ in range(1, number_of_lines + 1):
    line = input()

    if ',' and '.' and '_' in line:
        print(f'{line} is not pure!')
    else:
        print(f'{line} is pure.')