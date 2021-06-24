def is_armstrong_number(number):
    num_string = str(number)
    l = len(num_string)
    result = 0
    for c in num_string:
        result += pow(int(c), l)

    return result == number
