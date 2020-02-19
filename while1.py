"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
        usver_say = input(f'Как дела? ')
        if usver_say == 'Хорошо':
            break
        else:
            print(f'В смысле {usver_say.lower()}?')


def main():
    ask_user()

    
if __name__ == "__main__":
    main()
