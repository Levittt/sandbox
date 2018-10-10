n= int(input("Введите n: "))
s=0
for i in range(n,0,-1):
    print((' '*(n-(s+1))),('*'*(s+1)),end ='')
    s=s+1
    print()
    