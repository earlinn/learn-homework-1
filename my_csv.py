import csv

my_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open('my_csv.csv', 'w', encoding='cp1251', newline='') as f:
    fields = ['name', 'age', 'job']
    writing = csv.DictWriter(f, fields, delimiter=';')
    writing.writeheader()
    for person in my_list:
        writing.writerow(person)
