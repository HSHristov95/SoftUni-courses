year = int(input())

while True:
    year += 1
    found_digits = ''
    is_happy_year = True

    for digit in str(year):
            if digit in found_digits:
                is_happy_year = False
                break
            found_digits += digit
    if is_happy_year:
        break

print(year)