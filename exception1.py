"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

from random import choice


def ask_user():
    talk = {
      "Как дела?": "Хорошо!", 
      "Что делаешь?": "Программирую", 
      "На каком языке?": "На python", 
      "А зачем?": "Потому что могу", 
      "А спать когда?": "Никогда", 
      "Что ты можешь": "Все, что захочешь", 
      "Правда?": "Неправда", 
      "Какой?": "Да любой", 
      "Почему?": "По кочану", 
      "А ты?": "А чего сразу я?", 
      "Любой?": "Любой, не боись", 
      "Ты кто?": "Нормально же общались"
    }
    answers = [
      "Нехороший вопрос", 
      "Опять нехороший вопрос", 
      "А этот вопрос уже лучше", 
      "А это вообще не вопрос", 
      "Не вопрос", 
      "Ты серьезно?", 
      "?"
    ]
    while True:
        usver_say = input('Задай мне какой-нибудь вопрос. ')
        try:
            while True:
                if usver_say in talk:
                    usver_say = input(f'{talk[usver_say]}\n')
                if usver_say == '?':
                    return "Вот и поговорили!"
                if usver_say not in talk:
                    talk[usver_say] = choice(answers)
                    usver_say = input(f'{talk[usver_say]}\n')
        except KeyboardInterrupt:
            print('Пока!')
            break


def main():
    print(ask_user())

 
if __name__ == "__main__":
    main()
