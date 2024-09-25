day = int(input('Введите ваш день рождения:'))
month = int(input('Введите ваш месяц рождения:'))

if (day in range(21, 32) and month == 3) or (day in range(1, 21) and month == 4):
    print('Ваш знак зодиака - овен')
elif (21 <= day <= 30 and month ==4 ) or (1 <= day <= 21 and month == 5):
    print('Ваш знак зодиака - телец')
elif (22 <= day <= 31 and month == 5) or (1 <= day <= 21 and month == 6):
    print('Ваш знак зодиака - близнецы')
elif (22 <= day <= 30 and month == 6) or (1 <= day <= 22 and month == 7):
    print('Ваш знак зодиака - рак')
elif (23 <= day <= 31 and month == 7) or (1 <= day <= 21 and month == 8):
    print('Ваш знак зодиака - лев')
elif (22 <= day <= 31 and month == 8) or (1 <= day <= 23 and month == 9):
    print('Ваш знак зодиака - дева')
elif (24 <= day <= 30 and month == 9) or (1 <= day <= 23 and month == 10):
    print('Ваш знак зодиака - весы')
elif (24 <= day <= 31 and month == 10) or (1 <= day <= 22 and month == 11):
    print('Ваш знак зодиака - скорпион')
elif (23 <= day <= 30 and month == 11) or (1 <= day <= 22 and month == 12):
    print('Ваш знак зодиака - стрелец')
elif (23 <= day <= 31 and month == 12) or (1 <= day <= 20 and month == 1):
    print('Ваш знак зодиака - козерог')
elif (21 <= day <= 31 and month == 1) or (1 <= day <= 19 and month == 2):
    print('Ваш знак зодиака - водолей')
elif (20 <= day <= 29 and month == 2) or (1 <= day <= 20 and month == 3):
    print('Ваш знак зодиака - рыбы')
else:
    print('Ошибка')
