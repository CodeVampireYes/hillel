import string

input_user = 't!e@s#t t%e^s&t'

input_clean = input_user.translate(str.maketrans('', '', string.punctuation))

hashtag_conversion = input_clean.title().replace(' ', '')

hashtag = f'#{hashtag_conversion[:140]}'

print(hashtag)
