import random

def quicksort(nums):
    def helper(nums, lo, hi):
        if lo < hi:
            j = partition(nums, lo, hi)
            helper(nums, lo, j - 1)
            helper(nums, j + 1, hi)

    helper(nums, 0, len(nums) - 1)
    return nums

def partition(nums, lo, hi):
    i, j = lo + 1, hi
    while True:
        while i < hi and nums[i] <= nums[lo]:
            i += 1
        while j > lo and nums[j] >= nums[lo]:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[lo], nums[j] = nums[j], nums[lo]
    return j

data = [random.randint(1, 10) for _ in range(10000)]
print(quicksort(data))
