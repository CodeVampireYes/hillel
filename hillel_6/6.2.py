user_input_number = int(input("Введите количество секунд: "))

count_days = user_input_number // 86400
remaining_seconds = user_input_number % 86400
count_hours = remaining_seconds // 3600
remaining_seconds %= 3600
count_minutes = remaining_seconds // 60
count_seconds = remaining_seconds % 60

count_days = str(count_days)
count_hours = str(count_hours)
count_minutes = str(count_minutes)
count_seconds = str(count_seconds)

day = []

for el in count_days:
    day.append(el)

declension_word_day = ''

if day[-1] == '1' and (len(day) == 1 or day[-2] != '1'):
    declension_word_day = 'день'
elif day[-1] in ['2', '3', '4'] and (len(day) == 1 or day[-2] != '1'):
    declension_word_day = 'дні'
else:
    declension_word_day = 'днів'

print(f'{count_days} {declension_word_day}, {count_hours.zfill(2)}:{count_minutes.zfill(2)}:{count_seconds.zfill(2)}')
