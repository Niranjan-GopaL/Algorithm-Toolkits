from math import sqrt
from collections import deque


def sieve(n):
    global is_prime 
    is_prime = [True] * (n + 1)

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False


def generate_numbers(num):
    primes = []
    digits = list(str(num))

    for i in range(4):
        tmp_digit = digits[i]

        for j in range(10):
            if j != int(tmp_digit):
                digits[i] = str(j); new_num = int("".join(digits))

                if is_prime[new_num]:
                    primes.append(new_num)
        digits[i] = tmp_digit


    primes = [i for i in primes if len(str(i)) == 4]
    return primes


def bfs(n,target):
    q = deque([(n,0)])
    visited = set()

    while q:
        num,depth = q.popleft()
        print("\n---------Queue iteration from {num} --------------\n")


        print(f' Prime popped from stack : {num} and the current depth is : {depth}\n')

        if num == target:
            return depth

        if num not in visited:
            visited.add(num)
            q.extend([

                (i,depth+1) 
                for i in generate_numbers(num)
                
            ])
            print(f' Generated numbers for {num} are : {generate_numbers(num)}\n')




# start,target = map(int, input().split())
# in order to generate is_prime() array 
start,target = (1033,8179)
sieve(10000)
print(f'All primes : {[i for i in range(10000) if is_prime[i] ]} ')

print(bfs(start,target ))