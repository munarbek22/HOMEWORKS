mentors = ["Тимур", "Арсен", "Гулина",  "Даниель"]
print('Нажмите на клавишу 1 чтобы добавить имя.', ' клавишу 2 чтобы заменить ментора.', ' клавишу 3 чтобы чтобы удалить ментора из списка.', ' клавишу 0 чтобы выйти.')
while True:
    print(mentors)
    command = input('Введите команду: ')
    if command.isnumeric():
        command = int(command)
    if command == 1:
        name_1 = input('Имя должно содержать не более 15 букв. Введите имя: ').title()
        if len(mentors) > 10:
            print('Список менторов уже заполнен!')
        elif len(name_1) < 15 and name_1 not in mentors:
            mentors.append(name_1)
        else:
            print('Имя содержит больше 15 букв или имя занят! ')

    if command == 2:
        name_2 = input('Введите имя которое хотите заменить: ').title()
        newname = input(f'Имя должно содержать не более 15 букв.Введите имя которое хотите добавить вместо {name_2} :')

        if name_2 not in mentors:
            print('Введенное имя нет в списке!')
        elif len(newname) < 15 and newname  not in mentors:
            mentors[mentors.index(name_2)] = newname
        else:
            print('Имя содержит больше 15 букв или имя занят! ')
    elif command == 3:
        name_3 = input('Введите имя или индекс которое хотите удалить: ').title()
        if name_3.isalpha() and name_3 in mentors:
            mentors.remove(name_3)
        elif name_3.isnumeric():
            mentors.pop(int(name_3))
    elif command == 0:
        print(tuple(mentors))
        print('Выход...')
        break
    else:
        print('Введите команду правильно! 1-добавить, 2-изменить, 3-удалить, 0-выход')



