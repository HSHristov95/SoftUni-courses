numbers = input().split()

def even_numbers(n):
    return n % 2 == 0

even_nums = list(filter(even_numbers, map(int,numbers)))

print(even_nums)