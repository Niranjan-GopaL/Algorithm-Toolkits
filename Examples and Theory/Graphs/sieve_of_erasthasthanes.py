from math import sqrt
from time import time


# Traditional way to generate prime numbers less than n :- O(n^3/2)
def is_prime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True


def prime_smaller_than(n):
    for i in range(2,n):
        if is_prime(i):
            print(i,end=" " )




# Sieve of erasthasthanes :- O(nlog(logn))
def sieve(n):
    is_prime = [True] * (n + 1)

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    count = 0
    for i in range(1000, n+1):
        if is_prime[i]:
            print(i, end=" ")
            count += 1

    # print(f'\nNumber of 4 digit prime numbers are : {count}')

n = 10000
# prime_smaller_than(n)

for i in range(100000):
    sieve(n)
'''


0 -- 
0 -- 
0 -- 
0 -- 
0 -- 
0 -- 
0 -- 
0 -- 
0 -- 
0 -- 
0 -- 
    

'''