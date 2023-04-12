def FindRank(l,elem):
    for i in range(l):
        if i > elem :
            count += 1
    print(rank)


count = 0
# (Rank defined as number of elements greater than iteself) + 1
rank = 1 + count

l = list(map(int, input().split()))
elem_whose_rank_is_req = int(input())
FindRank(l,elem_whose_rank_is_req)