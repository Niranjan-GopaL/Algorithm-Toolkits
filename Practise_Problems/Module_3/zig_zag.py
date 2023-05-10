# Lool at Leetcode explanation for the math it's pretty simple and humble 
from math import floor,log2

def pathInZigZagTree( label):

    level = floor(log2(label))
    ans = [label]

    while label!=1:
        c = label - 2**level
        pos = c//2
        if level&1:
            label = 2**(level-1)+(2**(level-1)-pos-1)
        else:
            label = 2**(level) - 1 - pos
        level -= 1
        ans.append(label)
    return ans[::-1]


