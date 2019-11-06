# при определении объекта можно ставить поля и модификаторы доступа 
# + абстрагирование когда составляем млдель, надо брать только самые важные свойства, которые мы описываем
# список студентов на физ-ре, сдача зачета, определенное кол-во раз присесть (рандом кол-во), метод сделать упражнение
# базовый класс студент, наследники мальчики (12-20) и девочки  (8-15)
# список 100 студентов, заполнен случайно
# для каждого студента вызвать метод, посмотреть, сколько человек сдало зачет
# метод скажи сколько надо
# свойства студента: фио и группа 

import random

boys = ['Извеков','Подберёзный','Путин','Милос','Иванов', 'Петров','Кошкин','Ложкин']
girls = ['Литвинова','Медведева','Кардашьян','Кошкина','Симонова','Мармеладова','Виноградова']

class Student:
    def __init__(self):
        self.surname = ''
        self.name = ''
        self.middle_name = ''
        self.group = ''
        
class Boy(Student):
    def __init__(self):
        Student.__init__(self)

    def standart(self):
        return 30

    def do_exercise(self):
        return random.randint(0,100)
    
class Girl(Student):
    def __init__(self):
        Student.__init__(self)

    def standart(self):
        return 25

    def do_exercise(self):
        return random.randint(0,70)

students = []
for i in range(0,100,1):
    human = random.randint(0,1)
    
    if human == 0:
        human = Boy()
        human.surname = boys[random.randint(0,len(boys)-1)]
    else:
        human = Girl()
        human.surname = girls[random.randint(0,len(girls)-1)]

    students.append(human) 

passed = 0
for i in students:
    if i.do_exercise() > i.standart():
        passed += 1

print(passed)
