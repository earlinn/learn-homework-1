"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
        print('Как дела?')
        usver_say = input()
        if usver_say == 'Хорошо':
            return
        usver_say = usver_say.lower()
        print(f'В смысле {usver_say}?')
    

def main():
    ask_user()

    
if __name__ == "__main__":
    main()
