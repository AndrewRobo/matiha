#!/usr/bin/env python3
def try_input():
    while 1 :
        x=input("какое либо число =====>")
        try:
            x=int(x) 
            break      
        except:
            print("некоректный ввод")  
            continue
    return(x)        
#############################################################################################################
def nod_evklid_div(a,b):
     x,y=a,b
     if y>x:
         x,y=y,x
     z=1
     while z>0:
         z=x%y
         x,y=y,z
     return(x)
###################################################################################################################
def nod_evklid_minus(a,b):
     x,y=a,b
     if y>x:
         x,y=y,x
     z=1
     while z>0:
         z=x-y
         x=z
         if y>x:
             x,y=y,x
     return(x)
###################################################################################################################
def reheto(x):
     s0=list(range(2,x+1))
     for f in s0:
         if f>x**0.5:
             break    
         for g in s0[s0.index(f)+1:]:
             if ((g%f)==0):
                 s0.remove(g)
     return(s0)
#######################################################################################################################
def faktorial(x):
     h=1
     for g in range(1,x+1):
         h*=g
     return(h)
###################################################################################################################
def razlogenie(x):
     s=reheto(x)
     h=x
     d=[]
     while h>1:

         for k in s:
             t=h/k
             if t == int(t):
                 h=t
                 d.append(k)
     return(d) 
#########################################################################################################################################################
def razlogenie2(x):

     s=reheto(x)
     l = []          # тут мы сохраняем список простых множителей числа на которые разлагаем x
     y = x 
     while y > 1 :
         n = s[0]
    #     print("y=",y," делим на ",n)
         v = y / n
         if v == int(v):
            y = v 
            l.append(n)
       #     print("разделилось на ",n)
         else:
            s = s[1:]
       #     print("НЕ разделилось на", n )
    # print(l)
     return(l)
######################################################################################################################################################################
def nok_chit(x,y):
     v=1.5
     if y>x:
         x,y=y,x
     p=x
     while v != int(v):
         v=p/y
         if v != int(v):
             p=p+x
     return(p)       
############################################################################################################################
def nok_razlogenie(x,y):
    i = razlogenie2(x)
    o = razlogenie2(y)
    for q in i:
        for m in o:
            if q == m:
                o.remove(m)         
    for p in o:        
        i.append(p)
    g=1
    for h in i:
       g *= h
    return(g)
#################################################################################################################
def nod_razlogenie(x,y):
    i = razlogenie2(x)
    o = razlogenie2(y)
    print("i",i)
    print("o",o)
    aqw=[]
    for ip in i:
        print("ip",ip)
        for op in o:
            print(" op",op,'<=>',"ip =",ip)
            if ip == op:
                print("o",o)
                print("aqw",aqw)

                aqw.append(op)
                o.remove(op) 
                
                print("aqw",aqw)
                print("o",o)

                break
    print("##################################")
    g=1
    for u in aqw:
        g*=u
    print("НОД (",x,y,")=",aqw,"=",g)




























