command = input()
num1 = int(input())
num2 = int(input())

def calculation(action, a, b):

    if action == 'multiply':
        return a * b
    elif action == 'divide':
        return int(a / b)
    elif action == 'add':
        return a + b
    elif action == 'subtract':
        return a - b

print(calculation(command, num1, num2))