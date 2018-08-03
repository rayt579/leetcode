'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_in_rotated_sorted_array(nums, target)

    def search_original(self, nums, target):
        if not nums or len(nums) == 0:
            return -1

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[lo]:
                if nums[mid] > target and target >= nums[lo]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] <= nums[hi]:
                if nums[mid] < target and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1

    def search_in_rotated_sorted_array(self, nums, target):
        if not nums:
            return -1

        rot = self.find_rotation_point(nums)
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            rotmid = (mid + rot) % len(nums)
            if nums[rotmid] < target:
                lo = mid + 1
            elif nums[rotmid] > target:
                hi = mid - 1
            else:
                return rotmid
        return -1


    def find_rotation_point(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo

arr = [4,5,6,7,0,1,2]
arr_empty = []
arr_nil = None
sol = Solution()
print('Expect 4: {}'.format(sol.search(arr, 0)))
print('Expect 0: {}'.format(sol.search(arr, 4)))
print('Expect 6: {}'.format(sol.search(arr, 2)))

print('Expect -1: {}'.format(sol.search(arr_nil, 2)))
print('Expect -1: {}'.format(sol.search(arr_empty, 2)))

arr_even_len = [4, 5, 2, 3]
print('Expect 0: {}'.format(sol.search(arr_even_len, 4)))
print('Expect 1: {}'.format(sol.search(arr_even_len, 5)))
print('Expect 2: {}'.format(sol.search(arr_even_len, 2)))
print('Expect 3: {}'.format(sol.search(arr_even_len, 3)))
arr_three = [5, 1, 3]
print('Expect 0: {}'.format(sol.search(arr_three, 5)))
print('Expect 2: {}'.format(sol.search(arr_three, 3)))


print('Expect -1: {}'.format(sol.search([4,5,6,7,0,1,2], 3)))
