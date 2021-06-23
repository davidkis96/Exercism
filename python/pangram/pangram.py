import string


def is_pangram(sentence):
    if len(sentence) == 0:
        return False

    sentence = sentence.lower()

    for char in string.ascii_lowercase:
        if sentence.count(char) == 0:
            return False

    return True
