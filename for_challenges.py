# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']
print('\n'.join(names))


print()


# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём.

names = ['Оля', 'Петя', 'Вася', 'Маша']
names_lens = [len(name) for name in names]
names_dict = dict(zip(names, names_lens))
for name in names_dict:
    print(name + ':', names_dict[name])

print()

# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
names_gender = ['мужской' if is_male[name] else 'женский' for name in names]
names_gender_dict = dict(zip(names, names_gender))
for name in names_gender_dict:
    print(name + ': пол', names_gender_dict[name])

print()

# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# В группе 2 ученика.
# В группе 3 ученика.

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
print(f'Всего {len(groups)} группы.')
for group in range(len(groups)):
    print(f'В группе {group + 1} - {len(groups[group])} ученика.')

print()
# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят.
# Пример:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
for group in range(len(groups)):
    group_students = ', '.join(groups[group])
    print(f'Группа {group + 1}: {group_students}')
