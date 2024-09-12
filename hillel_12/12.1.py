import re
import codecs


def delete_html_tags(html_file, result_file='cleaned.txt', remove_empty_lines=True):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_content = file.read()
    cleaned_text = re.sub(r'<[^>]+>', '', html_content)

    if remove_empty_lines:
        cleaned_lines = [line.strip() for line in cleaned_text.splitlines() if line.strip()]
        cleaned_text = '\n'.join(cleaned_lines)

    with codecs.open(result_file, 'w', 'utf-8') as output_file:
        output_file.write(cleaned_text)


delete_html_tags('draft.html', 'cleaned.txt')
