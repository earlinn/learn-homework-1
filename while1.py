"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def ask_user():
    usver_say = input('Как дела?\n')
    while True:
        if usver_say == 'Хорошо':
            return 'Пока!'
        usver_say = usver_say.lower()
        usver_say = input(f'В смысле {usver_say}?\n')


def main():
    print(ask_user())

    
if __name__ == "__main__":
    main()
