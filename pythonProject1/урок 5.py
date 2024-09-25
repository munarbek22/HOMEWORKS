# Словари - dictionary, множества.
# {key: value}

# student = {
#     'name': 'azamat',
#     'age': 19,
#     'weight': 67.4
# }
#
# print(student.keys())
# print(student.values())
# print(student.items())

 # for key, value in student.items():
 #    print(f'{key}: {value}')


# print(student)
# """add"""
# student['surname'] = 'musaev'
# student.update({'hobby': ['chess', 'boxing'], 'married': False})
#
# """edit"""
# student['age'] += 1
# student['hobby'] = ['english', 'books']
#
# """delete"""
# student.pop('hobby')
# del student['married']


# print(student['name'])
# print(student['age'])

# numbers_1 = [1, 2, 3, 2, 4, 3, 1, 5, 1]
# numbers_2 = {1, 2, 3, 2, 4,  3, 1, 5, 1 }
#
# print(numbers_1)
# print(numbers_2)

# num = int('1892') + int('7')

# beshbarmak = {"мясо", "лук", "тесто"}
# plov = {"мясо", "рис", "морковь"}
#
# print(beshbarmak.union(plov))
# print(beshbarmak.difference(plov))
# print(beshbarmak.intersection(plov))