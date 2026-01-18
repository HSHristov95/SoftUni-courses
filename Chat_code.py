number_of_codes = int(input())

for _ in range(number_of_codes):
    code = int(input())

    if code == 88:
        print('Hello')
    elif code == 86:
        print('How are you?')
    elif code < 88:
        print('GREAT!')
    else:
        print('Bye.')