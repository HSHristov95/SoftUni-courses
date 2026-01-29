nums = [int(n) for n in input().split()]

def min_max_sum(a):
    return f'The minimum number is {min(a)}\nThe maximum number is {max(a)}\nThe sum number is: {sum(a)}'

print(min_max_sum(nums))