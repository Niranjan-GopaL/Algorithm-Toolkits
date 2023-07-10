def f2():
    print(l)

def f1():
    for elem in l:
        elem[0] = "HWAAAAA"
    

l = [[0,1,'a'],[1,2,'b']]
f1()
f2()