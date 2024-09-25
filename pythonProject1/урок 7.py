# Lambda функциию Обработка исключений.


# try:
#     print(2 * 'geeks')
# except:
#     print('Найдена ошибка')
# else:
#     print('ok')
# finally:
    # print('Проверка завершена')


# lambda_func = lambda n1, n2: n1 + n2
#
# def def_func(n1, n2):
#     return n1 + n2
#
#
# print(lambda_func(2, 3))
# print(def_func(2, 3))
# print(type(lambda_func))
# print(type(def_func))

# print(len([1, 2, 3]))
# print(len('geeks'))
#
# print(help(len))
# print(len.__doc__)

# word = [23, 32, 56, 879, 4]
#
# def len1(objects):
#     counter = 0
#     for i in objects:
#         counter += 1
#     return counter
#
# print(len1(word))


# def get_square(length: int, width: int) -> int:
#     """
#     Принимает длину и ширину, возвращает площадь.
#     """
#     return length * width
#
#
# print(help(get_square))

# def up_first_letter(word: str):
#     return word.title()

#
# def show_words(func, objects):
#     for i in objects:
#         print(func(i))
#
# cities = ['tokmok', 'karakol', 'kant', 'kemin']
# show_words(lambda word: word.title(), cities)

students = ['bakai', 'liza', 'begimai', 'almaz', 'tagai', 'munarbek']
print(students)

map_students = list(map(lambda name: name.upper(), students))
print(map_students)

filter_students = list(filter(lambda name: 'g' in name, students))
print(filter_students)

sorted_students = sorted(students, key=lambda name: name[1])
print(sorted_students)
# #
# show_words(len, cities)
# show_words(up_first_letter, cities)


# days = 1
# expenses = {}
# #
# while days < 8:
#     try:
#         expenses[days] = int(input(f'Введите расход дня №{days}: '))
#         days += 1
#     except:
#         print('Введите только числа!')
# # days = 1
# # expences = []
# for day, expence in expenses.items():
#     print(f'{day}: {expence} сом.')
#
# print(sum(expenses.values()))
# print(sum(expenses.values() ))
