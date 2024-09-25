# ЗАДАНИЕ №1
# def nearest_number(objects: iter, number):
#     return_n = sorted(objects, key=lambda obj: abs(obj - number))
#     return(number, return_n)
#
#
# print(nearest_number([5, 20.18, 103, 4], 27))


# ЗАДАНИЕ №2
# words = ['beautiful', 'world', 'sun', 'cat', 'elephant']
# print(words)
# short_words = list(filter(lambda word: len(word) < 6, words))
#
# print(short_words)
#
#
# words = ['beautiful', 'world', 'sun', 'cat', 'elephant']
# print(words)
# len_words = list(map(lambda word: len(word), words))
# print(len_words)



# ЗАДАНИЕ №3
# def write_index(objects):
#     while True:
#         user_input = (input('Введите индекс для вывода элемента или exit чтобы выйти: '))
#         if user_input == 'exit':
#             print('Выход...')
#             break
#         if user_input.isnumeric():
#             try:
#                 index = int(user_input)
#                 element = objects[index]
#                 print(f'Элемент с индексом {user_input}: {element}')
#             except:
#                 print(f'Ошибка! Индекс вне диапазона. Введите индекс от 0 до {len(objects) - 1}.')
#         else:
#                 print('Ошибка! Введите индекс (целое число) или exit для выхода. ')
# data = [12, 3, 81, 22, 4, 9, 1, 28, 8, 15, 18]
# print(write_index(data))