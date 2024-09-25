# Списки, . Индексы и срезы.
# Встроенные функции к наборам элементов.
# Списковое включение List comprehension.
# Кортежи.

# numbers = (23, 7, 10, 2.5, 5, 2.5)
# print(type(numbers))

# """Встроенные функции к наборам элементов"""
# print(len(numbers))
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))

students = ['ariet', 'munarbek', 'aimir', 'ablai', 'bakai']
# students_2 = [name.title() for name in students if 'r' in name]
print(students)
# print(students_2)
#
# students_copy = students.copy()
# students[0] = 'aman'
# print(id(students))
# print(id(students_copy))
# print(students is students_copy)
# print(students_copy == students)
print(students)
# print(students_copy)

"""add"""
# students.append('halima')
# students.insert(2,'magomedkamil')
# students.extend(['islam', 'abdulloh'])

"""edit"""
# students.reverse() .change places
students.sort()
# students[1] = 'tagai'
# students[:2] = ['almira', 'tynchtykbek']

"""delete"""
# students.remove('ablai')
# students.pop(0)
# deleted = students.pop(0)
# del students [:2]
# print(deleted)
print(students)


"""индексы"""
# print(students[0])
# print(students[-1])

"""срезы [start:stop:step]"""
# print(students[1:3])
# print(students[:3])
# print(students[3:])
# print(students[::-1])
# print(students[])
# print(students[])