def find_number():

    print('Загадайте число от 0 до 100 и я постараюсь угадать')

    less_number = 1
    biggest_number = 100
    attempts = []
    attempt_count = 0

    while True:
        number = (less_number + biggest_number) // 2
        attempts.append(number)
        attempt_count += 1

        user_input = input(f'Вы загадали число {number}? (да/больше/меньше) если да, то программа перенесет информацию в файл results.txt: ').lower()
        if user_input == 'да':
            with open('results.txt', 'w') as file:
                file.write(f'Количество попыток: {attempt_count}\n'
                           f'Список попыток: {attempts}\n'
                           f'Загаданное число: {number}')
            print(f'Программа угадала {number} число за {attempt_count} попыток')
            break
        elif user_input == "больше":
            less_number = number + 1
        elif user_input == "меньше":
                biggest_number =number - 1
        else:
            print("Неверный ввод. Пожалуйста, ответьте 'да', 'больше' или 'меньше'.")
            attempts.pop()

find_number()