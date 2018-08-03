'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
'''

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.find_minimum_iterative_brief(nums)

    def find_minimum_iterative(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if 0 < mid < len(nums) - 1 and nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif mid == len(nums) - 1 and nums[mid] < nums[0]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                hi = mid - 1
            else:
                lo = mid + 1
        return nums[0]

    def find_minimum_recursive(self, nums):
        def helper(lo, hi):
            if nums[lo] <= nums[hi]:
                return nums[lo]
            mid = lo + (hi - lo)//2
            if nums[mid] >= nums[lo]:
                return helper(mid + 1, hi)
            else:
                return helper(lo, mid)
        return helper(0, len(nums) - 1)

    def find_minimum_iterative_brief(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

sol = Solution()
nums = [3,4,5,1,2]
#print('Expect 1: {}'.format(sol.findMin(nums)))

nums2 = [4,5,6,7,0,1,2]
#print('Expect 0: {}'.format(sol.findMin(nums2)))

nums3 = [2,1]
print('Expect 1: {}'.format(sol.findMin(nums3)))
