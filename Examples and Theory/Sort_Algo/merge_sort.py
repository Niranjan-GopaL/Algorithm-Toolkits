def merge(l1,l2):
    l=[]
    i=j=0
    while i<len(l1) and j<len(l2):
        if l1[i] < l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
    if i < len(l1):
        l.extend(l1[i:])
    elif j < len(l2):
        l.extend(l2[j:])
    return l


def merge_sort(li,l,h):
    if len(li) == 1:
        return li
    
    mid_idx = (l+h)//2

    left = merge_sort(li,l,mid_idx-1)
    right = merge_sort(li,mid_idx,h)

    return merge(left,right)


l = list(map(int, input().split()))

print(merge_sort(l,0,len(l)-1))