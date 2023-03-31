def merge(arr1, arr2):
	m = len(arr1)
	n = len(arr2)
	arr3 = []

	i = 0
	j = 0
	while i < m and j < n:
		# comparing strings
		if arr1[i] < arr2[j]:
			arr3.append(arr1[i])
			i += 1
		else:
			arr3.append(arr2[j])
			j += 1
	while i < m:
		arr3.append(arr1[i])
		i += 1
	while j < n:
		arr3.append(arr2[j])
		j += 1
	return arr3

# Function to mergeSort 2 arrays
def merge_sort(arr, lo, hi):
	if lo == hi:
		return [arr[lo]]
	mid = lo + (hi - lo) // 2
	arr1 = merge_sort(arr, lo, mid)
	arr2 = merge_sort(arr, mid + 1, hi)

	arr3 = merge(arr1, arr2)
	return arr3


t = int(input())
s_list = []

for i in range(t):
    s = input().lower()
    s_list.append(s)

for s in s_list:
    lt = []
    # MASTERPIECE TO GENERATE ALL ROTATIONS OF A STRING
    s = s + s
    for idx in range(len(s)//2):
        temp = s[idx : (len(s)//2)+idx]
        lt.append(temp)

    lt = merge_sort(lt , 0 , len(lt) - 1)
    print(lt[-1])
