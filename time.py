# класс время, свойства: минуты и часы. метод добавления кол-ва минут, часы и минуты закрытые
# установить часы и минуты
# изменить время, минуты и часы 

class Time:
    def __init__(self):
        self.__hours = 0
        self.__minutes = 0

    def get_minutes(self):
        print(self.__minutes,' Минут')

    def get_hours(self):
        print(self.__hours, ' Часов')

    def set_hours(self,hours):
        self.__hours = hours

    def set_minutes(self,minutes):
        self.__minutes = minutes

    def change_minutes(self,minutes):
        self.__minutes += minutes
        if self.__minutes >= 60:
            self.__minutes -= 60
            self.__hours += 1

    def change_hours(self,hours):
        if hours > 24:
            print('look at dis duuuuuude OH NO NO NO')
        else:
            self.__hours += hours
            
            

t = Time()

t.set_hours(5)
t.set_minutes(59)

t.change_minutes(55)
t.get_hours()
t.get_minutes()

