def is_valid(isbn):
    isbn = isbn.replace('-', '')

    if len(isbn) != 10:
        return False

    result = 0
    for i in range(-1, -11, -1):
        char = isbn[::-1][abs(i) - 1]
        if not char.isdigit():
            if char != 'X' or char != isbn[-1]:
                return False
            else:
                char = '10'

        result += int(char) * abs(i)

    return result % 11 == 0


