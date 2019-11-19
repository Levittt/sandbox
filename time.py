# класс время, свойства: минуты и часы. метод добавления кол-ва минут, часы и минуты закрытые
# установить часы и минуты
# изменить время, минуты и часы 
# след. задача - модуль, наследник - день,месяц,год (високосный, февраль, 30-31 числа)
class Time:
    def __init__(self):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0

    def get_hours(self):
        return self.__hours

    def get_minutes(self):
        return self.__minutes

    def get_seconds(self):
        return self.__seconds

    def set_hours(self,hours):
        if (hours < 24) and (hours >= 0):
            self.__hours = hours
        else:
            raise Exception('hours can not be more than 24')

    def set_minutes(self,minutes):
        if (minutes < 60) and (minutes >= 0):
            self.__minutes = minutes
        else:
            raise Exception('minutes can not be more than 60')

    def set_seconds(self,seconds):
        if (seconds < 60) and (seconds >= 0):
            self.__seconds = seconds
        else:
            raise Exception('seconds can not be more than 60')

    def change_hours(self,hours):
        self.__hours = (self.__hours + hours) % 24

    def change_minutes(self,minutes):
        hours = (self.__minutes + minutes) // 60
        self.change_hours(hours)
        self.__minutes = (self.__minutes + minutes) % 60

    def change_seconds(self,seconds):
        minutes = (self.__seconds + seconds) // 60
        self.change_minutes(minutes)
        self.__seconds = (self.__seconds + seconds) % 60

t = Time()

t.set_hours(-4)
t.set_minutes(59)
t.set_seconds(59)
#t.change_minutes(1)
t.change_seconds(1)


g = Time()

g.set_hours(-3)
g.set_minutes(0)
g.set_seconds(0)


print(g.get_hours(), ' Часов ', end='')
print(g.get_minutes(), ' Минут ', end='')
print(g.get_seconds(), ' Секунд')


print(t.get_hours(), ' Часов ', end='')
print(t.get_minutes(), ' Минут ', end='')
print(t.get_seconds(), ' Секунд')



