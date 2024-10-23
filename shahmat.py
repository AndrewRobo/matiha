n=2  # n>2 strok
m=4  # #m<=10^8 stolbcov

#1 slon v levom verhnem ugl

ll=[]
mm=min(n,m)+1
aa=range(2,mm)
print(aa)

for i in range(2,mm):
    a=[i,i]
    ll.append(a)

    b=[n-i,i]
    if a==b :
        ll.append([0,0])
    else:
        ll.append(b)


    c=[i,m-i]
    if c==a:
        ll.append([0,0])
    elif b==c:
            ll.append([0,0])
    else:
            ll.append(c)

    d=[n-i,m-i]
    if d==a:
        ll.append([0,0])
    elif d==b:
            ll.append([0,0])
    elif d==c:
            ll.append([0,0])
    else:
        ll.append(d)

print(ll)