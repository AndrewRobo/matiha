#!/usr/bin/env python3

w=int(input("введи число болше чем 3 "))
k=2
while k<w/2:
    i=w%k
    print(w,":",k,"=",w//k," остаток ",i)
    if i==0:
        print("число разделилось нацело найден делитель Ж_Ж",k)
    k=k+1

