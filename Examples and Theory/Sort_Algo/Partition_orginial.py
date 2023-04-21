# LEARN HOW TO IMPORT :-
# from random import a , b ,c   => rnadint()  <----- IMP
#  import random    => random.randint()

from random import randint , randrange

# Original code that takes pivot as First elemrnt
def partition_FQS (list_1,left,right):
    pivot = left
    small = left
    for i in range(small,right+1):
        if list_1[i] <= list_1[pivot]:
            list_1[i] , list_1[small] = list_1[small] , list_1[i]
            small += 1
    list_1[pivot] , list_1[small-1] = list_1[small-1] , list_1[pivot]
    return small

def FQS(list_1,left,right):
    if left < right:
        pvt_idx = partition_FQS(list_1,left,right)
        FQS(list_1,left,pvt_idx-1)
        FQS(list_1,pvt_idx+1,right)
    
# Original code that takes pivot as Last elem
def partition_LQS(list_1,left,right):
    small = left
    for i in range(left, right):
        if list_1[i] <= list_1[right]:
            list_1[i] , list_1[small] = list_1[small] , list_1[i]
            small +=1
    list_1[right] , list_1[small] = list_1[small] , list_1[right]
    return small

def LQS(list_1,left,right):
    if left < right:
        pvt_idx = partition_LQS(list_1,left,right)
        LQS(list_1,left,pvt_idx-1)
        LQS(list_1,pvt_idx+1,right)

def RQS(li,l,r):
    if l < r:
        # BOTH l and r and included in randint 
        p = randint(l,r) 
        li[p],li[l] = li[l],li[p]
        k = partition_FQS(li,l,r)
        RQS(li,l,k-1)
        RQS(li,k+1,r)


l = list(map(int, input().split()))

# Use whichever you want to
# LQS(l,0,len(l)-1)
# FQS(l,0,len(l)-1)
# RQS(l,0,len(l)-1)
print(l)