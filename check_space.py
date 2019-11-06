#интерфейс, у эл-а есть отступы справа и слева, проверка, влезает ли эл-т в размеры экрана

class Elem:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.margin_left = 0 
        self.margin_right = 0

class Contain(Elem):
    def __init__(self):
        Elem.__init__(self)
        self.arr = []

class Container(Contain):
    def __init__(self):
        Contain.__init__(self)
        self.title = ''

    def space(self):
        flag = True
        
        sum_width = 0
        sum_height = 0
        for i in range(0,len(self.arr),1):
            sum_width += self.arr[i].width
            sum_height += self.arr[i].height

        if sum_width > self.width:
            flag = False
        elif sum_height > self.height:
            flag = False
        else:
            for i in range(0,len(self.arr),1):
                if hasattr(self.arr[i], 'space'):
                    if self.arr[i].space() == False:
                        flag = False
                        
        return flag 

page = Container()
page.width = 1920
page.height = 800
page.title = 'simple page'

button = Elem()
button.width = 300
button.height = 100
button.margin_left = 50
button.margin_right = 50
page.arr.append(button)

picture = Elem()
picture.width = 100
picture.height = 100
picture.margin_left = 50
picture.margin_right = 50
page.arr.append(picture)

block = Container()
block.width = 200
block.height = 200
block.margin_left = 20
block.margin_right = 20
page.arr.append(block)

figure = Elem()
figure.width = 300
figure.height = 50
figure.margin_left = 10
figure.margin_right = 10
block.arr.append(figure)

if page.space() == False:
    print('нет места')
else: 
    print('места хватает')
