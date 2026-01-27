int_numbers = [float(i) for i in input().split()]

def abs_numbers(numbers):
    result = []

    if numbers:
        for i in numbers:
            result.append(abs(float(i)))
    else:
        result = 'Error'

    return result

print(abs_numbers(int_numbers))