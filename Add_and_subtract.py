num1 = int(input())
num2 = int(input())
num3 = int(input())

def sum_numbers(a,b):
    return a+b

def subtract(a,b):
    return a-b

def add_and_subtract(sum_numbers,subtract):
    return sum_numbers-subtract

print(subtract(sum_numbers(num1, num2),num3))