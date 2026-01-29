start_char = input()
end_char = input()

def ascii_result(start,finish):
    result = []

    for i in range(ord(start)+1, ord(finish),1):
        char = chr(i)
        result.append(char)

    return ' '.join(result)

print(ascii_result(start_char, end_char))