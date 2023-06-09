def mergeSort(arr, n):
	# A temp_arr is created to store
	# sorted array in merge function
	temp_arr = [0]*n
	return _mergeSort(arr, temp_arr, 0, n-1)

# This Function will use MergeSort to count inversions
def _mergeSort(arr, temp_arr, left, right):
	inv_count = 0
	if left < right:
		mid = (left + right)//2
		inv_count += _mergeSort(arr, temp_arr,left, mid)
		inv_count += _mergeSort(arr, temp_arr,mid + 1, right)
		inv_count += merge(arr, temp_arr, left, mid, right)
	return inv_count


def merge(arr, temp_arr, left, mid, right):
	i = left	 # Starting index of left subarray
	j = mid + 1 # Starting index of right subarray
	k = left	 # Starting index of to be sorted subarray
	inv_count = 0

	while i <= mid and j <= right:
		# no inversion
		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			# Inversion will occur.
			temp_arr[k] = arr[j]
			inv_count += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	# Copy the sorted subarray into Original array
	for loop_var in range(left, right + 1):
		arr[loop_var] = temp_arr[loop_var]

	return inv_count


arr = [1, 20, 6, 4, 5]
n = len(arr)
result = mergeSort(arr, n)
print("Number of inversions are", result)