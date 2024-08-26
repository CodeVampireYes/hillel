import string


def is_palindrome(text: str) -> bool:
    clear_text = text.lower().translate(str.maketrans('', '', string.punctuation)).replace(' ', '')
    return clear_text == ''.join(reversed(clear_text))


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
