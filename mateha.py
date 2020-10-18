#!/usr/bin/env python3

import random
print('немухлевать        ясно!!!')
sp=[3,4,6,7,8,9]
for d in range(0,4):
    # получаем  случайное целое
    # число в диапазоне от ста
    # тысяч до девятсот девяносто
    # девяти тысяч девятсот девяносто девяти
    a=random.randint(100000,999999)

    i=random.choice(sp)
    #print("i первая цифра",i)
    f=random.choice(sp)
    #print("f вторая цифра",f)
    o=f*10+i
    print(o)
    h=a*o
    print(h)

