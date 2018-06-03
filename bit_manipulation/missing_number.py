'''
https://leetcode.com/problems/missing-number/description/
'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        expected_sum = len(nums) * (len(nums) + 1) // 2
        return expected_sum - sum(nums)

    def missing_number_bit(self, nums):
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ nums[i] ^ i
        return res

    def missing_number_bsearch(self, nums):
        nums.sort()
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (hi - lo)//2 + lo
            if nums[mid] > mid:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo


sol = Solution()
print('expected 2: {}'.format(sol.missingNumber([3,0,1])))
print('expected 8: {}'.format(sol.missingNumber([9,6,4,2,3,5,7,0,1])))
print('expected 2: {}'.format(sol.missing_number_bit([3,0,1])))
print('expected 8: {}'.format(sol.missing_number_bit([9,6,4,2,3,5,7,0,1])))
print('expected 2: {}'.format(sol.missing_number_bsearch([3,0,1])))
print('expected 8: {}'.format(sol.missing_number_bsearch([9,6,4,2,3,5,7,0,1])))
