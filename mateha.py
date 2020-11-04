#!/usr/bin/env python3

import random

print("\033[31m {}\033[0m  ".format('примеры на деление'))
sp=[2,3,4,5,6,7,8,9]
 
# в пепременрй q будем запаминать делители
# чтобы исключать повторения 
q=[]
#print(len (q))
while len(q) < 4:

# получаем  случайное целое
# число в диапазоне от ста
# тысяч до девятсот девяносто
# девяти тысяч девятсот девяносто девяти
    a=random.randint(10000,99999)
    
    i=random.choice(sp)
    #print("i первая цифра",i)
    f=random.choice(sp)
    #print("f вторая цифра",f)
    while i==f:
        #print("i=",i,",f=",f,"если цифры равны то меняем одну из них")
        f=random.choice(sp)
    o=f*10+i # из 2 случайных цифр сделали число -делитель 
    if o in q:
        #print(o,"есть в списке",q)
       pass
    else:
        q.append(o)
        h=a*o
        print("\033[33m",len(q),")",h,":",o)

