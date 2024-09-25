
# while True:
#     word = input("Введите слово: ").lower()
#
#     if word == "выход" or word == "exit":
#         print('exit...')
#         break
#     letters = 0
#     for letter in word:
#         letters += 1
#     cons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y",
#             "z", "б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "щ",
#             "ш"]
#     number_of_cons = 0
#     for letter in word:
#         if letter in cons:
#             number_of_cons += 1
#     vow = ["е", "ё", "ю", "я", "э", "ы", "a", "и", "у", "о", "e", "i", "o", "u", "а"]
#     number_of_vow = 0
#     for letter in word:
#         if letter in vow:
#             number_of_vow += 1
#
#     vow_percent = round(number_of_vow / letters * 100, 2)
#     cons_percent = round(number_of_cons / letters * 100, 2)
#     print("Количество букв:", letters)
#     print("Количество согласных:", number_of_cons)
#     print("Количество гласных:", number_of_vow)
#     print("Гласные/Согласные:", vow_percent, "% /", cons_percent, "%")


mentors = ["Тимур", "Арсен", "Гулина", "Даниель"]


def print_menu():
    print("1) Добавление")
    print("2) Изменение")
    print("3) Удаление")
    print("0) Выход")


def add_mentor():
    if len(mentors) >= 10:
        print("Список полон. Невозможно добавить больше менторов.")
        return

    name = input("Введите имя ментора: ").strip().capitalize()
    if len(name) > 15:
        print("Имя должно содержать не более 15 букв.")
        return

    if name in mentors:
        print("Имя уже есть в списке.")
    else:
        mentors.append(name)
        print(f"Имя '{name}' добавлено.")


def modify_mentor():
    old_name = input("Введите имя, которое нужно заменить: ").strip().capitalize()
    if old_name not in mentors:
        print("Имя не найдено в списке.")
        return

    new_name = input("Введите новое имя: ").strip().capitalize()
    if len(new_name) > 15:
        print("Имя должно содержать не более 15 букв.")
        return

    if new_name in mentors:
        print("Имя уже есть в списке.")
    else:
        index = mentors.index(old_name)
        mentors[index] = new_name
        print(f"Имя '{old_name}' изменено на '{new_name}'.")


def remove_mentor():
    print("Выберите вариант удаления:")
    print("1) По индексу")
    print("2) По имени")
    choice = input("Введите номер варианта: ").strip()

    if choice == "1":
        try:
            index = int(input("Введите индекс ментора: "))
            if 0 <= index < len(mentors):
                removed_mentor = mentors.pop(index)
                print(f"Ментор '{removed_mentor}' удален.")
            else:
                print("Неверный индекс.")
        except ValueError:
            print("Введите корректное число.")
    elif choice == "2":
        name = input("Введите имя ментора: ").strip().capitalize()
        if name in mentors:
            mentors.remove(name)
            print(f"Ментор '{name}' удален.")
        else:
            print("Имя не найдено в списке.")
    else:
        print("Некорректный выбор.")


def main():
    while True:
        print_menu()
        choice = input("Введите команду: ").strip()

        if choice == "1":
            add_mentor()
        elif choice == "2":
            modify_mentor()
        elif choice == "3":
            remove_mentor()
        elif choice == "0":
            mentors_tuple = tuple(mentors)
            print(f"Итоговый список менторов: {mentors_tuple}")
            break
        else:
            print("Некорректная команда. Пожалуйста, выберите снова.")


