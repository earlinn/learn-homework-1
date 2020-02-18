"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры 
  и выводя на экран результаты

"""

def main():
    def compare_two_strings(first_string, second_string):
        if type(first_string and second_string) == str:
            if first_string == second_string:
                return 1
            elif len(first_string) > len(second_string):
                if second_string == 'learn':
                    return 'learn spam' # both statements are valid 
                return 2
            elif second_string == 'learn':
                return 3
        else:
            return 0
        return 'spam' # for unconditioned statements


    for function_call in [['iyh', 'ylf'], [0, 7], ['typo', 999], \
      ['spam', 'spam'], ['spam', 'egg'], ['eggs', 'learn'], \
        ['longread', 'learn']]:
        print(compare_two_strings(function_call[0], function_call[1]))

    
if __name__ == "__main__":
    main()
