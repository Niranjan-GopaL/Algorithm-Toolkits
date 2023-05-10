# recursion takes exponential time

def fib(n):
    if n<2:
        return n
    else:
        return (fib(n-1) + fib(n-2)) % 10
    
# For n>100 it takes few seconds

# 2^(n/2) < T(n) < 2^n  => TAKES EXPONENTIAL TIME!!!
n_ = int(input())
print(fib(n_))