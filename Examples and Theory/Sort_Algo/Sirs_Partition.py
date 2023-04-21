def Partition(li,l,r):
    pivot = li[l]
    i = l+1
    j = r
    while i <= j:
        while i <= j and li[i] <= pivot:
            i += 1
        while i <= j and li[j] >= pivot:
            j -= 1
        if i < j:
            li[i],li[j] = li[j],li[i]
            i += 1
            j -= 1
 
    i -= 1
    li[i] , li[l] = li[l] , li[i]
    return i
