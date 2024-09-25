# Операторы: принадлежности, назначения. Циклы.


"""операторы назначения"""
# number = 10
# number = number + 5 (старый вариант)
# number += 5
# number /= 2
# number **= 2
# number %= 2
# print(number)

"""операторы принадлежности"""
# word = 'GEEKS'
# print('h' in word)
# print('G' in word)
# print(2 in range(1, 11))
# print(52 in range(1, 11))

# rounds = 0
# while rounds < 50:
#     rounds += 1
#     if rounds == 25:
#          print('finish')
#          break
#     if rounds in range(17, 21):
#         continue
#     print('geeks'.upper(), rounds)

# attempts = int(input('enter attempts: '))
# while attempts > 0:
#     print(f'attempts: {attempts}')
#     time = input('enter time: ').lower()
#     if time == 'exit':
#         print('stop!')
#         break
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('Вы ввели неверные данные')
#     if time in 'morning утро day день evening вечер ':
#         attempts -= 1


# word = 'Kyrgyzstan'
# for letter in word:
#     if letter == 'z':
#         break
#     if letter in 'yrz':
#         continue
#     print(letter)
#
# for number in range(1, 11):
#     print(number)

# attempts = int(input('enter attempts:'))
# for attempt in range(1, attempts+1):
#     print(f'попытка № {attempt}:')
#     time = input('enter time: ').lower()
#
#     if time == 'morning' or time == 'утро':
#         print('good morning')
#     elif time == 'day' or time == 'день':
#         print('good afternoon')
#     elif time == 'evening' or time == 'вечер':
#         print('good evening')
#     else:
#         print('Hello')
