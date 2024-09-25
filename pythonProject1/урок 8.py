# Контекстный менеджер "with", работа с файлами
# w - write, re-write
# a - add
# x - создает только новые файлы

# file = open('new_file.txt', 'w')
# file.write('Бишкек, Кыргызстан')
# file.close()

# with open('new_file.txt', 'a') as file:
#     file.write('\nвторая строка')

# with open('file.txt', 'x') as new_file:
#     new_file.write('243636457645')

# with open('new_file.txt', 'r') as file:
    # print(file.read())

# from time import sleep
#
# with open('new_file.txt', 'r') as file:
#     for letter in file.readlines():
#         sleep(1)
#         print(letter, end='')

from random import choice

topics = tuple(range(1,9))
students = [7, 14, 6, 10, 4, 3, 1, 15, 18]


with open('ratings.txt', 'w') as new_file:
    new_file.write('ИТОГИ УСТНОГО ОПРОСА ГРУПЫ: 46-3\n')

while students:
    print('студентов осталось', len(students))
    random_student = choice(students)
    random_topic = choice(topics)
    name = input(f'student № {random_student}: ').title()
    rate = input(f'mark for {name}, topic: {random_topic}')
    with open('ratings.txt', 'a') as results:
        results.write(f'\n{name} - topic: {random_topic} mark: {rate}')
    students.remove(random_student)
