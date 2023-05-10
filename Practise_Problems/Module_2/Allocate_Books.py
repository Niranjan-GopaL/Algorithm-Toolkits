def isPossible(arr, n, m, curr_min):
	studentsRequired = 1
	curr_sum = 0

	for i in range(n):
		if (arr[i] > curr_min):
			return False
		if (curr_sum + arr[i] > curr_min):
			studentsRequired += 1
			curr_sum = arr[i]

			if (studentsRequired > m):
				return False
		else:
			curr_sum += arr[i]
	return True



def findPages(arr, n, m):

	sum = 0
	if (n < m):
		return -1

	for i in range(n):
		sum += arr[i]

	print(sum)
	start, end = 0, sum
	result = 10**9
	while (start <= end):

		print(result)
		mid = (start + end) // 2

		print(isPossible(arr,n,m,mid))
		if (isPossible(arr, n, m, mid)):
			result = mid
			end = mid - 1
		else:
			start = mid + 1

	return result

n = int(input())
arr = list(map(int , input().split()))
m = int(input())

print("Minimum number of pages = ",
	findPages(arr, n, m))