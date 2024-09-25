# Функции: виды параметров, возвращение данных, виды аргументов.


"""схема функции"""
# определение наименование(параметры):
#     тело функции
#     возвращение объекта
#
# вызов функции
# наименование(аргументы)

# lenght = 8
# width = 5
# square_3 = lenght * width
# print(square_3)
#
# lenght = 20
# width = 12
# square_hall = lenght * width
# print(square_hall)

# def get_data(name, surname='неизвестно'):
#     print(f'name: {name} surname: {surname}')
#
# get_data('tilek', 'erikov')
# get_data('alina', 'amanova')
# get_data(name='japarov', surname='bakai')
# get_data('umut')
#
# def get_square(lenth, width):
#     square = lenth * width
#     return square
#
# square_3 = get_square(8, 5)
# square_hall = get_square(20, 12)
# print(square_3, square_hall, sep='\n')
# #
# def num(*args):
#     return sum(args)
#
# print(num(2, 4, 5, 60, 26))
#
#
# def menu(**kwargs):
#     return kwargs
#
# print(menu(eat= 'pizza', drink= 'cola'))

# number = int(312.0 - 2 * 6)
# print(number)

# print(type('def'))
# print(100 if 300 // 2 == 150 else 200)
# print(float("python"))

# geeks_in = ['бишкек', 'Ощ', 'кара балта', '9 мкр']
# geeks_in = geeks_in[::-1]
# print(geeks_in)
# geektech = {
#     'name': 'Geektech',
#     'adress': 'Токтогула 175',
#     'courses': {'Backend', 'Android'}
# }
#
# geeks = dict(name='GEEKS', adress='Ибраимова 103')
# geektech.update(geeks)
# geeks = geektech.copy()
# geeks['courses'].update(['Fronted', 'IOS'])
# print(geeks)

# counter = 5
#
# while counter != 0:
#     print('geeks')
#     counter -= 1

# geeks = 2018
# current_year = int(input('enter current year'))
#
# if (geeks - current_year) > 5:
#     print('more 5 year')
# else:
#     pass
# elif (geeks - current_year) < 5:
#     print('less')

# for i in range(1, 10+1):
#     if i > 7:
#         print(i)
#     else:
#         print('False')


# def calculator(num1: float, operator: str, num2: float) -> float:
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             return "Ошибка: на ноль делить нельзя."
#         return num1 / num2
#     else:
#         return "Ошибка: неподдерживаемый оператор. Используйте '+', '-', '*', '/'."
#
#     return calculator()


# def calculator(num1: float, operator: str, num2: float) -> float:
#     """
#     Выполняет арифметические операции с двумя числами в зависимости от оператора.
#
#     :param num1: Первое число (float).
#     :param operator: Арифметический оператор (str). Должен быть одним из '+', '-', '*', '/'.
#     :param num2: Второе число (float).
#     :return: Результат арифметической операции (float), если операция успешна.
#              Если возникла ошибка, возвращает None.
#     """
#     # Проверка типа данных
#     if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
#         print("Ошибка: оба числа должны быть типа int или float.")
#         return none
#
#     # Выполнение арифметической операции в зависимости от оператора
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             print("Ошибка: на ноль делить нельзя.")
#             return None
#         return num1 / num2
#     else:
#         print("Ошибка: неподдерживаемый оператор. Используйте '+', '-', '*', '/'.")
#         return None
#
#
#
#
#
#
#
# def calculator(num1: float, operator: str, num2: float) -> float:
#     """
#     Выполняет арифметические операции с двумя числами в зависимости от оператора.
#
#     :param num1: Первое число (float или int).
#     :param operator: Арифметический оператор (str). Должен быть одним из '+', '-', '*', '/'.
#     :param num2: Второе число (float или int).
#     :return: Результат арифметической операции (float), если операция успешна.
#              Если возникла ошибка, возвращает float('nan') для обозначения ошибки.
#     """
#     # Проверка типа данных
#     if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
#         return float('nan')  # Возвращаем NaN (Not a Number) для обозначения ошибки
#
#     # Выполнение арифметической операции в зависимости от оператора
#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         if num2 == 0:
#             return float('nan')  # Возвращаем NaN для деления на ноль
#         return num1 / num2
#     else:
#         return float('nan')  # Возвращаем NaN для неподдерживаемого оператора
#
# print(calculator(num1: float, operator: str, num2: float))
# Примеры использования функции
# print(calculator(10, '+', 5))  # 15.0
# print(calculator(10, '/', 0))  # nan
# print(calculator(10, 'x', 5))  # nan
# print(calculator('a', '+', 5))  # nan


# def calculator(num1: float, operator: str, num2: float) -> float:
#     """
#     Функция выполняет арифметические операции между двумя числами.
#
#     Параметры:
#     num1 (float): Первое число.
#     operator (str): Оператор ('+', '-', '*', '/', '**', '//', '%').
#     num2 (float): Второе число.
#
#     Возвращает:
#     float: Результат выполнения арифметической операции или None в случае ошибки.
#     """
#     try:
#         # Обработка арифметических операций
#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             if num2 == 0:
#                 print("Ошибка: Деление на ноль невозможно.")
#                 return None
#             return num1 / num2
#         elif operator == '**':
#             return num1 ** num2
#         elif operator == '//':
#             if num2 == 0:
#                 print("Ошибка: Деление на ноль невозможно.")
#                 return None
#             return num1 // num2
#         elif operator == '%':
#             if num2 == 0:
#                 print("Ошибка: Деление на ноль невозможно.")
#                 return None
#             return num1 % num2
#         else:
#             print("Ошибка: Недопустимый оператор. Используйте '+', '-', '*', '/', '**', '//', '%'.")
#             return None
#     except ValueError:
#         print("Ошибка: Неверные значения для чисел.")
#         return None
#
#
# # Пример использования функции:
# result = calculator(10, '/', 0)
# if result is not None:
#     print(f"Результат: {result}")

# num_1 = float(input('Введите первое число: '))
# operator = input('Введите операцию: ')
# num_2 = float(input('Введите второе число: '))
#
# def calculator(num1: float, operator: str, num2: float) -> float:
#     if operator == '+':
#         return num_1 + num_2
#
#
#     elif operator == '-':
#         return num_1 - num_2
#
#
#     elif operator == '*':
#         return num_1 * num_2
#
#
#     elif operator == '/':
#         return num_1 / num_2
#
#     else:
#         return
#     return calculator()

# Базовый класс SuperHero
class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
        self.damage = damage
        self.fly = False  # Новое свойство fly по умолчанию False

    def hero_name(self):
        print(f"Hero's name is {self.name}")

    def double_health(self):
        self.health_points *= 2
        print(f"{self.name}'s health is now {self.health_points}")

    def __str__(self):
        return f"Nickname: {self.name},\nSuperpower: {self.superpower},\nHealth: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


# Класс SkyHero (воздушный герой)
class SkyHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.element = "Sky"  # Свойство, уникальное для небесного героя

    # Изменение метода double_health (полиморфизм)
    def double_health(self):
        self.health_points **= 2  # Возведение здоровья в квадрат
        self.fly = True  # Изменяем fly на True
        print(f"{self.name}'s health is now squared to {self.health_points}. Fly: {self.fly}")

    # Новый метод, который выводит фразу
    def true_phrase(self):
        print(f"True in the True_phrase: {self.fly}")


# Класс SpaceHero (космический герой)
class SpaceHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.element = "Space"  # Свойство, уникальное для космического героя

    # Изменение метода double_health (полиморфизм)
    def double_health(self):
        self.health_points **= 2  # Возведение здоровья в квадрат
        self.fly = True  # Изменяем fly на True
        print(f"{self.name}'s health is now squared to {self.health_points}. Fly: {self.fly}")

    # Новый метод, который выводит фразу
    def true_phrase(self):
        print(f"True in the True_phrase: {self.fly}")


# Создание объектов классов SkyHero и SpaceHero
sky_hero = SkyHero("Zephyr", "Sky Lord", "Mastery over winds", 180, "Feel the wrath of the storm!", 70)
space_hero = SpaceHero("Nova", "Cosmic Guardian", "Control over stars", 250, "The universe bows before me!", 90)

# Вызов новых методов
sky_hero.double_health()  # Возведение здоровья в квадрат и изменение fly на True
sky_hero.true_phrase()  # Вывод фразы
space_hero.double_health()  # Возведение здоровья в квадрат и изменение fly на True
space_hero.true_phrase()  # Вывод фразы


# Класс Villain, наследуемый от SuperHero
class Villain(SuperHero):
    people = 'monster'  # Изменение значения people

    def gen_x(self):
        pass  # Метод пока ничего не делает

    # Метод, который возводит урон в степень
    def crit(self, other):
        if hasattr(other, 'damage'):
            other.damage **= 2
            print(f"{other.name}'s damage after critical hit is now {other.damage}")


# Создание объекта класса Villain
villain = Villain("Thanos", "Mad Titan", "Infinity Gauntlet", 300, "I am inevitable!", 120)

# Применение метода crit на объект другого класса (например, SpaceHero)
villain.crit(space_hero)  # Возведение урона SpaceHero в квадрат
