'''
https://leetcode.com/problems/maximum-product-subarray/description/
'''

class Solution(object):
    def max_product_brute_force(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        maximum_product = nums[0]
        for i in range(1, len(nums)):
            prod = nums[i]
            maximum_product = max(maximum_product, prod)
            for j in range(i - 1, -1, -1):
                prod *= nums[j]
                maximum_product = max(maximum_product, prod)
        return maximum_product

    def maxproduct_allocate_space(self, nums):
        if not nums:
            return 0

        max_prod = nums[0]
        largest_prod = [0] * len(nums)
        smallest_prod = [0] * len(nums)
        largest_prod[0], smallest_prod[0] = nums[0], nums[0]

        for i in range(1, len(nums)):
            largest_prod[i] = max(nums[i], nums[i] * largest_prod[i - 1], nums[i] * smallest_prod[i - 1])
            smallest_prod[i] = min(nums[i], nums[i] * largest_prod[i - 1], nums[i] * smallest_prod[i - 1])
            max_prod = max(max_prod, largest_prod[i])

        return max_prod

    def maxProduct(self, nums):
        if not nums:
            return 0

        max_prod = nums[0]
        largest_prod, smallest_prod = nums[0], nums[0]

        for i in range(1, len(nums)):
            temp = largest_prod
            largest_prod = max(nums[i], nums[i] * largest_prod, nums[i] * smallest_prod)
            smallest_prod = min(nums[i], nums[i] * temp, nums[i] * smallest_prod)
            max_prod = max(max_prod, largest_prod)

        return max_prod

sol = Solution()
print('Expecting 6: {}'.format(sol.maxProduct([2,3,-2,4])))
print('Expecting 0: {}'.format(sol.maxProduct([-2,0,-1])))
print('Expecting 12: {}'.format(sol.maxProduct([-4,-3,-2])))
