'''
https://leetcode.com/problems/product-of-array-except-self/description/
'''


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        output = [None] * len(nums)
        prod_before, prod_after = 1, 1

        for i in range(len(nums)):
            output[i] = prod_before
            prod_before *= nums[i]

        for j in range(len(nums) - 1, -1, -1):
            output[j] *= prod_after
            prod_after *= nums[j]

        return output


sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))
