'''
Writing algo hurts my head so Imma dev instead.

'''

# FLEX BY DOING ALL THIS IN A SINGLE LIST COMPHRENSION
def bubble_sort(arr : list) -> list:
    # for i_index , i_item in enumerate(arr[:max_number_of_comparisons_req]):
        # if i_item > arr[i_index+1]:
            # i_item , arr[i_index+1] = arr[i_index+1] , i_item
            
    for max_number_of_comparisons_req in range(len(arr)-1, 0, -1):
        for j in range(max_number_of_comparisons_req):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1], arr[j]


            


l = [1,2,3,4,5]
print(bubble_sort(l[::-1]))