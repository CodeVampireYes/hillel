import string

input_user = input('Введите строку:' )
#input_user = 'Should, I. subscribe? Yes!'

hashtag_conversion = input_user.title().replace(' ', '').translate(str.maketrans('','', string.punctuation))

print(f'#{hashtag_conversion[:140]}')
