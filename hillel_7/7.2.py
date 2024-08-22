def correct_sentence(text: str) -> str:
    if text:
        text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    corrected_text = []
    capitalize_next = False

    for char in text:
        if capitalize_next and char.isalpha():
            corrected_text.append(char.upper())
            capitalize_next = False
        else:
            corrected_text.append(char)
        if char == '.':
            capitalize_next = True

    return ''.join(corrected_text)


# Test the function
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
