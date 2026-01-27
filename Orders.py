product = input()
number_of_products = int(input())

def price_tab(order, number):
    if order == 'coffee':
        return f'{number * 1.50:.2f}'
    elif order == 'water':
        return f'{number * 1.00:.2f}'
    elif order == 'coke':
        return f'{number * 1.40:.2f}'
    elif order == 'snacks':
        return f'{number * 2.00:.2f}'

print(price_tab(product, number_of_products))