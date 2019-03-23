class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in differences:
                return [i, differences[diff]]
            else:
                differences[diff] = i
        return None


sol = Solution()
res = sol.twoSum([2,7,9,11], 9)
print(res)
        
