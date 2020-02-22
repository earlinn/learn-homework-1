# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

students_names = []

for person in range(len(students)):
    students_names.append(students[person]['first_name'])

students_unique_names = set(students_names)

for person in students_unique_names:
    print(f'{person}: {students_names.count(person)}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2
print()


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

students_names = []

for person in range(len(students)):
    students_names.append(students[person]['first_name'])

students_unique_names = set(students_names)
students_names_frequency = []

for person in students_unique_names:
    auxilary_list = []
    auxilary_list.append(students_names.count(person))
    auxilary_list.append(person)
    students_names_frequency.append(auxilary_list)

students_names_frequency.sort()
most_frequent_name = students_names_frequency[-1][1]

print(f'Самое частое имя среди учеников: {most_frequent_name}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

print()

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

school_list = []
for school_class in school_students:
    students_list = []
    for student in school_class:
        students_list.append(student.get('first_name'))
    school_list.append(students_list)
#print(school_list)

for school_class in range(len(school_list)):
    students_set = set(school_list[school_class])
    name_frequency, most_frequent_name = 0, ''
    for student in students_set:
            if school_list[school_class].count(student) > name_frequency:
                name_frequency, most_frequent_name = school_list[school_class].count(student), student
    print(f'Самое частое имя в классе {school_class + 1}: {most_frequent_name}')


# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

print()

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for school_class in school:
    boy, girl = 0, 0
    class_number = school_class['class']
    for student in school_class['students']:
        if is_male[student['first_name']]:
            boy += 1
        else:
            girl += 1
    print(f'В классе {class_number} {girl} девочки и {boy} мальчика.')


# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

print()

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for school_class in school:
    boy, girl = 0, 0
    class_number = school_class['class']
    for student in school_class['students']:
        if is_male[student['first_name']]:
            boy += 1
        else:
            girl += 1
    school_class['boys'] = boy
    school_class['girls'] = girl
more_boys_first = sorted(school, key=lambda x: -x['boys'])
more_girls_first = sorted(school, key=lambda x: -x['girls'])
more_boys_first_class = more_boys_first[0]['class']
more_girls_first_class = more_girls_first[0]['class']
print(f'Больше всего мальчиков в классе {more_boys_first_class}.')
print(f'Больше всего девочек в классе {more_girls_first_class}.')

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
