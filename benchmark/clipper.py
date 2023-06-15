import pyautogui as p
import time

time.sleep(7)
p.typewrite(
'''
from typing import List


class FenwickTree:
    def _init_(self, N: int):
        self.N = N
        self.arr = [0] * N
        
    def sum(self, i: int):  # i is 1-indexed
        s = 0
        while i:
            s += self.arr[i-1]
            i -= i & -i
        return s
    
    def add(self, i: int, k):  # i is 1-indexed
        while i <= self.N:
            self.arr[i-1] += k
            i += i & -i


def numTeams(rating):
    N = len(rating)
    fw = FenwickTree(N)
    bw = FenwickTree(N)
    
    r = sorted((n, i) for i, n in enumerate(rating))
    for n, i in reversed(r):
        bw.add(N-i, 1)
    
    ans = 0
    for n, i in r:
        bw.add(N-i, -1)
        a, b = fw.sum(i+1), bw.sum(N-i)
        ans += a * b + (i - a) * (N - i - b - 1)
        fw.add(i+1, 1)
    return ans


ratings = [2, 5, 3, 4, 1]
answer = numTeams(ratings)
print("Number of teams:", answer)

'''
)
p.typewrite(['enter'])
