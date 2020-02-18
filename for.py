"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    from random import randint, choice
        

    # средний балл в классе
    def school_grade_point_average(school): 
        all_scores = []
        for classroom in school:
            all_scores += classroom['scores']
        grade_point_average = round(sum(all_scores) / len(all_scores), 2)
        return f'Средний балл по всей школе: {grade_point_average}.'


    # средний балл в школе
    def class_grade_point_average(scores): 
        return round(sum(scores) / len(scores), 2)
    

    # генератор школы
    def generate_school(max_num_of_classrooms, min_classroom, max_classroom): 
        sequence, school = ['a', 'b', 'c'], []
        classrooms = set(str(randint(1, 11)) + choice(sequence) \
          for i in range(max_num_of_classrooms))
        for classroom in classrooms:
            class_scores = {'school_class': classroom, 'scores': [randint(1, 5) \
                for student in range(randint(min_classroom, max_classroom))]}
            school.append(class_scores)
        return school
   

    # пользовательский ввод для создания школы
    classes = 'максимальное количество классов'
    min_num = 'минимальное количество учеников в классе'
    max_num = 'максимальное количество учеников в классе'
    my_school = list(
                     map(
                         int, 
                         input(f'Введите через пробел {classes}, {min_num} и {max_num}: ').split()
                         )
        )
    
    # создаем школу
    my_school = generate_school(my_school[0], my_school[1], my_school[2])
    
    # выводим средние баллы для созданной школы и классов в ней
    print(school_grade_point_average(my_school))
    print('-------------------------------------------')  
    for classroom in my_school:
        print(f"Средний балл в классе {classroom['school_class']}: {class_grade_point_average(classroom['scores'])}.")

    
if __name__ == "__main__":
    main()
