#!/usr/bin/env python3

i=3
b=int(input("до скольки мне искать? "))
q=[]
while i<=b: 
    q.append(i)
    i=i+3
print("найдено значений в диапазоне от 0 до",b,"-_-",len(q))
print(q) 
