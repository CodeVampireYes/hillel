def popular_words(text: str, words: list[str]) -> dict:
    word_list = text.lower().split()
    result_dict = {}
    for el in words:
        el = el.lower()
        result_dict[el] = word_list.count(el)
    return result_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
