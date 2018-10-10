n= int(input("Введите n: "))
for i in range(0,n,1):
    print('* ',end ='')
print()
for i in range(0,n-2,1):
    for i in range(0,n,1):
        if i==0 or i==n-1:
            print('* ',end ='')
        else:
            print('  ',end ='')
    print()
for i in range(0,n,1):
    print('* ',end ='')