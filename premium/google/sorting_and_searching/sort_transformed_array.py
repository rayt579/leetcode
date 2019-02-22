class Solution:
    def sortTransformedArray(self, nums: 'List[int]', a: 'int', b: 'int', c: 'int') -> 'List[int]':
        if not nums:
            return [0]

        nums = [a * x * x + b * x + c for x in nums]
        transformed = [0] * len(nums)
        lo, hi = 0, len(nums) - 1
        i = hi if a > 0 else lo
        while lo <= hi:
            if a > 0:
                if nums[lo] < nums[hi]:
                    transformed[i] = nums[hi]
                    hi -= 1
                else:
                    transformed[i] = nums[lo]
                    lo += 1
                i -= 1
            else:
                if nums[lo] < nums[hi]:
                    transformed[i] = nums[lo]
                    lo += 1
                else:
                    transformed[i] = nums[hi]
                    hi -= 1
                i += 1

        return transformed

sol = Solution()
res = sol.sortTransformedArray([-4, -2, 2, 4], 1, 3, 5)
print(res)
