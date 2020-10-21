#!/usr/bin/env python3

import random
print('примеры')
sp=[3,4,5,6,7,8,9]
for d in range(1,5):
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
        print("i=",i,",f=",f,"если цифры равны то меняем одну из них")
        f=random.choice(sp)
    o=f*10+i
    h=a*o
    print(d,"-",h,":",o)

