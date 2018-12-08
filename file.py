import csv

who = [{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
      {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
      {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
      ]

with open('file.csv', 'w', encoding='utf-8', newline='') as f:
    for man in who:
        writer = csv.DictWriter(f, man.keys())
        writer.writerow(man)
