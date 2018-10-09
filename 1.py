import math
a= float(input("Введи а "))
b= float(input("Введи б "))
c= float(input("Введи с "))
#ax^2+bx+c=0
D =(b*b-4*a*c)
if D<0:
    print ("нет корней")
elif D==0:
    x=(-b)/2*a
    print (x)
else:
    x1=(math.sqrt(D)-b)/2*a
    x2=(-(math.sqrt(D))-b)/2*a
    print (x1)
    print(x2)