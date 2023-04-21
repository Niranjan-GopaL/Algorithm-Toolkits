def swap(arr, index1, index2):
    arr[index1] , arr[index2] = arr[index2], arr[index1]

def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            swap(arr, swap_index, i)
    swap(arr, pivot_index, swap_index)
    return swap_index # return the index of the swap not the element

# Quick sort recursively on both sides of the pivot (one side at a time)
def quick_sort(arr, left, right):
    if left < right:
        pivot_index = pivot(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)  
        quick_sort(arr, pivot_index + 1, right)       


l = list(map(int, input().split()))
quick_sort(l,0,len(l)-1)

print(l)