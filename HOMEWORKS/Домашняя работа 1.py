monday = float(input('Введите расход за понедельник: '))
tuesday = float(input('Введите расход за вторник: '))
wednesday = float(input('Введите расход за среду: '))
thursday = float(input('Введите расход за четверг: '))
friday = float(input('Введите расход за пятницу: '))
saturday = float(input('Введите расход за субботу: '))
sunday = float(input('Введите расход за воскресенье: '))
summ = monday + tuesday + wednesday + thursday + friday + saturday + sunday
print(f'Общий расход за неделю: {summ}')
average = summ / 7
av_round = round(average, 1)
print(f'Средний расход в день: {av_round}')

if 1 <= summ <= 150:
    print('Потрачено малое количество денег')
elif 151 <= summ <= 500:
    print('Потрачено среднее количество денег')
elif 501 <= summ <= 999999999999999:
    print('Потрачено много денег')
else:
    print('Ничего не потрачено.')







# cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
#             "z", "б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "щ",
#             "ш"]
#
# vow = ["е", "ё", "ю", "я", "э", "ы", "a", "и", "у", "о", "e", "i", "o", "u", "а"]
#
# while True:
#     word = input('Введите слово: ').lower()
#     if word == 'exit' or word == 'выход':
#         print('exit...')
#         break
#     letters = 0
#     for letter in word:
#         letters += 1
#     print('Количество букв:', letters)
#     number_of_cons = 0
#     for letter in word:
#         if letter in cons:
#             number_of_cons += 1
#     print('Количество согласных букв', number_of_cons)
#     number_of_vow = 0
#     for letter in word:
#         if letter in vow:
#             number_of_vow += 1
#     print('Количество гласных букв', number_of_vow)
#
#     vow_percent = round(number_of_vow/letters * 100, 2)
#     cons_percent = round(number_of_cons/letters * 100, 2)
#     print('Гласные/Согласные: ', vow_percent, "%/", cons_percent, "%")


