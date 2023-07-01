from math import sqrt

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

    for i in range(2, n+1):
        if is_prime[i]:
            print(i, end=" ")


n = 100
prime_smaller_than(n)
sieve(n)