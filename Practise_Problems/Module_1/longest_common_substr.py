def compute_hash(substring, length):
    # Compute the hash value of a given substring using the Rabin-Karp algorithm
    # Returns a hash value
    hash_value = 0
    prime = 101
    for i in range(length):
        hash_value += ord(substring[i]) * pow(prime, i)
    return hash_value


def is_common_subarray(length, l1, m, l2, n):
    # Check if a given length of the substring appears in both arrays
    # Returns a Boolean value
    hash_set = set()
    for i in range(m - length + 1):
        hash_set.add(compute_hash(l1[i:i+length], length))
    for i in range(n - length + 1):
        if compute_hash(l2[i:i+length], length) in hash_set:
            return True
    return False


def find_largest_common_subarray(l1, m, l2, n):
    low = 0
    high = min(m, n)
    max_length = 0
    while low <= high:
        mid = (low + high) // 2
        if is_common_subarray(mid, l1, m, l2, n):
            max_length = mid
            low = mid + 1
        else:
            high = mid - 1
    return max_length

l1 = input().split()
l2 = input().split()
m = len(l1)
n = len(l2)

max_length = find_largest_common_subarray(l1, m, l2, n)
print(max_length)