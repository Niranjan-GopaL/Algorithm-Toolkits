def  f():
    t += 1      # doesn't work
    l.append(4) # works fine

def f1():
    print(l)

t = 0
l = [1,2,3]
f()
f()

f1()

f()
f()
f1()