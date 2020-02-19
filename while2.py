"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
from random import choice


def ask_user():
    talk = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", \
      "На каком языке?": "На python", "А зачем?": "Потому что могу", \
        "А спать когда?": "Никогда", "Что ты можешь": "Все, что захочешь", \
          "Правда?": "Неправда", "Какой?": "Да любой", "Почему?": "По кочану", \
            "А ты?": "А чего сразу я?", "Любой?": "Любой, не боись", \
              "Ты кто?": "Нормально же общались"}
    answers = ["Нехороший вопрос", "Опять нехороший вопрос", \
      "А этот вопрос уже лучше", "А это вообще не вопрос", "Не вопрос", \
        "Ты серьезно?", "?"]
    while True:
        usver_say = input(f'Задай мне какой-нибудь вопрос. ')
        if usver_say in talk:
            print(talk[usver_say])
        if usver_say == '?':
            break
        if usver_say not in talk:
            talk[usver_say] = choice(answers)
            print(talk[usver_say])
    print("Вот и поговорили!")


def main():
    ask_user()

 
if __name__ == "__main__":
    main()
