# cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
#             "z", "б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "щ",
#             "ш"]
# vow = ["е", "ё", "ю", "я", "э", "ы", "a", "и", "у", "о", "e", "i", "o", "u", "а"]
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





vowels = "aeiouаеёиоуыэюя"
consonants = "bcdfghjklmnpqrstvwxyzбвгджзклмнопрстфхцчшщ"

while True:
    word = input("Введите слово или 'exit' для выхода: ")

    if word.lower() == 'exit':
        print("Выход...")
        break

    letters = 0
    vowel = 0
    consonant = 0

    for letter in word:
        if letter.isalpha():
            letters += 1
            if letter.lower() in vowels:
                vowel += 1
            elif letter.lower() in consonants:
                consonant += 1

    if letters > 0:
        vowel_percentage = round((vowel / letters) * 100, 2)
        consonant_percentage = round((consonant / letters) * 100, 2)
    else:
        vowel_percentage = 0
        consonant_percentage = 0

    print(f"Общее количество букв: {letters}")
    print(f"Количество гласных: {vowel}")
    print(f"Количество согласных: {consonant}")
    print(f"Процент гласных: {vowel_percentage}%")
    print(f"Процент согласных: {consonant_percentage}%")