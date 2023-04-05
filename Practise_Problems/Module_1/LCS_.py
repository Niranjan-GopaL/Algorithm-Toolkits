base, MOD = 100_001, pow(2,31)-1

def rolling_hash(arr, i, size, seed,lookup):
    h = seed
    if i == 0:
        for j in range(size):
            h *= base
            h += arr[i+j]
            h %= MOD
    else:
        h -= arr[i-1]*lookup[size-1]
        h *= base
        h += arr[i+size-1]
        h %= MOD
    return h

def foundSubArray(size, lookup, nums1, nums2):
    # Base chosen: must be larger than maximum of nums1 and nums2; preferably prime
    # Mod: large enough to avoid overflow, should be prime
    # Go through all subarrays with length size in nums1, and record their hash values and the corresponding index
    seen = {}
    h = 0
    for i in range(len(nums1) - size + 1):
        h = rolling_hash(nums1, i, size, h,lookup)
        if h not in seen:
            seen[h] = []
        seen[h].append(i)

    # Check for nums2, see if any subarray of the same size is seen before
    h = 0
    for i in range(len(nums2) - size + 1):
        h = rolling_hash(nums2, i, size, h,lookup)
        if h in seen:
            for j in seen[h]:
                if nums1[j:j + size] == nums2[i:i + size]:
                    return True
    return False    

def findLength(nums1, nums2) -> int:
    m, n = len(nums1), len(nums2)
    lookup = []
    seed = 1
    for i in range(min(m,n)):
        lookup.append(seed)
        seed *= base
        seed %= MOD
    
    left, right, ans = 1, min(m, n), 0
    while left <= right:
        mid = (left + right) // 2
        if foundSubArray(mid , lookup, nums1, nums2):
            ans = mid  # Update answer
            left = mid + 1  # Try to expand size
        else:
            right = mid - 1  # shrink size
    return ans

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(findLength(nums1, nums2))