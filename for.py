"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from random import randint, choice


def school_grade_point_average(school): 
    # функция возвращает средний балл в школе
    all_scores = []
    for classroom in school:
        all_scores += classroom['scores']
    grade_point_average = round(sum(all_scores) / len(all_scores), 2)
    return f'Средний балл по всей школе: {grade_point_average}.'


def class_grade_point_average(school_class, scores): 
    # функция возвращает средний балл в классе
    average = round(sum(scores) / len(scores), 2)
    return f"Средний балл в классе {school_class}: {average}."


def generate_school(max_num_of_classrooms, min_classroom, max_classroom):
    # функция - генератор школы

    class_symbols, school = ['a', 'b', 'c'], []

    # создаем сами классы школы, убираем повторяющиеся
    classrooms = set(str(randint(1, 11)) + choice(class_symbols) \
        for i in range(max_num_of_classrooms))

    # создаем список оценок для каждого класса
    # каждый класс с оценками упаковываем в отдельный словарь
    # добавляем полученный словарь в школу
    for classroom in classrooms:
        class_scores = {
            'school_class': classroom, 
            'scores': [randint(1, 5) \
                for student in range(randint(min_classroom, max_classroom))]
        }
        school.append(class_scores)
    return school


def main():
    try:
        print('Введите через пробел:')
        print('- максимальное число классов,')
        print('- минимальное число учеников в классе,')
        print('- максимальное число учеников в классе')
        my_school = list(map(int, input().split()))
        if my_school[0] < 1 or my_school[1] < 1 or my_school[2] < 1:        
            raise ValueError
        if my_school[1] > my_school[2]:
            raise ValueError
        if len(my_school) != 3:
            raise ValueError
        
        # создаем школу
        my_school = generate_school(my_school[0], my_school[1], my_school[2])
    
        # выводим средние баллы для созданной школы и классов в ней
        print(school_grade_point_average(my_school))
        print('-' * 30)  
        for classroom in my_school:
            print(class_grade_point_average(classroom['school_class'], \
                classroom['scores']))
    except ValueError:
        print('\n' + 'Вводите только натуральные числа,' + '\n' \
            + 'максимум должен быть больше минимума,' + '\n' \
                + 'не забывайте пробел.')

    
if __name__ == "__main__":
    main()
