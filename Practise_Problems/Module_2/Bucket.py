l = list(map(int, input().split()))

c1=c2=c3=c4=c5=0
a=b=c=d=e=0
n = len(l)

for i in range(n):
    if a and b and c and d and e:
        c1 -= 1  
        c2 -= 1  
        c3 -= 1  
        c4 -= 1  
        c5 -= 1  
    else:
        if a:
            if i == a:
                c1 += 1
        else:
            a = i

        if b:
            if i == b:
                c1 += 1
        else:
            b = i

        if c:
            if i == c:
                c1 += 1
        else:
            c = i

        if d:
            if i == d:
                c1 += 1
        else:
            d = i

        if e:
            if i == e:
                c1 += 1
        else:
            e = i

if a:
    c_1 = 0
    for i in range(n):
        if i == a:
            c_1 += 1
            if c_1 == 3:
                print(a)
                break 

if b:
    c_2 = 0
    for i in range(n):
        if i == b:
            c_2 += 1
            if c_2 == 3:
                print(b)
                break            
if c:
    c_3 = 0
    for i in range(n):
        if i == c:
            c_3 += 1
            if c_3 == 3:
                print(c)
                break            
if d:
    c_4 = 0
    for i in range(n):
        if i == d:
            c_4 += 1
            if c_4 == 3:
                print(d)
                break            
if e:
    c_5 = 0
    for i in range(n):
        if i == e:
            c_5 += 1
            if c_5 == 3:
                print(e)
                break          