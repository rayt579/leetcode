class Solution:
    def longestConsecutive(self, nums):
        return self.longest_consecutive_linear(nums)
    
    def longest_consecutive_linear(self, nums):
        max_length = 0
        nums_set = set(nums)

        for num in nums:
            if num - 1 not in nums_set:
                current_num, current_streak = num, 0
                while current_num in nums_set:
                    current_streak += 1
                    current_num = current_num + 1
                max_length = max(max_length, current_streak)

        return max_length


    def longest_consecutive_sorting(self, nums):
        n = len(nums)
        max_length = 0
        i = 0

        nums.sort()
        while i < n:
            start, j = i, i + 1
            while j < n:
                if nums[i] == nums[j]:
                    start += 1
                    i += 1
                    j += 1
                elif nums[i] + 1 == nums[j]:
                    i += 1
                    j += 1
                else: 
                    break

            max_length = max(max_length, j - start)
            i = j

        return max_length

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))
