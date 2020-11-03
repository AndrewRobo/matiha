#!/usr/bin/env python3

w=int(input("введи первую цифру "))
e=int(input("введи вторую цифру "))
t=w/e
print(w,":",e,"=",t)

i=w%e
if i==0:
    print("число разделилось нацело",)
print("остаток ",i)

