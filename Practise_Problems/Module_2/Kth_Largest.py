# Quick_Select
def Quick_Select(l,r):
    pivot = li[r]
    small = l

    for i in range(l,r):
        if li[i] <= pivot:
            li[i],li[small] = li[small],li[i]
            small +=1
    # swapping pivot to  'small' position as it is now in the correct
    #  position as in that of the sorted array
    li[r],li[small] = li[small],li[r]

    # SMALL IS FINALLY AT correct position as in the sorted list's idx
    if k < small : return Quick_Select(l,small - 1)
    elif k > small : return Quick_Select(small+ 1,r)

    # Finally small will be at k
    else: return li[small]



# HERE K AND li ARE GLOBAL VARIABLE!!!!!!!!!
#  function can access them unlike in C
li = list(map(int , input().split()))
k = int(input())

# Since K largest => (len-k)th index in sorted array
k = len(li) - k
print(Quick_Select(0, len(li)-1))