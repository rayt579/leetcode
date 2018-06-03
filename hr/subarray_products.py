'''
https://leetcode.com/problems/subarray-product-less-than-k/description/
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, start = 0, 0
        prod = 1
        for end in range(len(nums)):
            prod *= nums[end]
            while start <= end and prod >= k:
                prod /= nums[start]
                start += 1
            count += end - start + 1
        return count

sol = Solution()
print('Expecting 8: {}'.format(sol.numSubarrayProductLessThanK([10,5,2,6],100)))

