import string


def first_word(text: str) -> str:
    split_text = text.split()
    first_word_spelled = []

    for index, el in enumerate(split_text[0]):
        count = 0
        if el.isupper() and index != 0:
            break
        if el not in string.punctuation or el == "'":
            first_word_spelled.append(el)

    if len(first_word_spelled) == 0 and len(split_text) > 1:
        return first_word(' '.join(split_text[1:]))

    result = ''.join(first_word_spelled)
    return result


# Test cases
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

