'''
https://leetcode.com/problems/jump-game/description/
'''

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_jump = True
        dist = nums[0]

        for i in range(1, len(nums)):
            if last_jump and dist > 0:
                last_jump = True
                dist = max(dist - 1, nums[i])
            else:
                last_jump = False

        return last_jump

    def can_jump_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        can_jump_at = {}
        def can_jump_recursive_memoize(i):
            if i in can_jump_at:
                return can_jump_at[i]
            if i == len(nums) - 1:
                can_jump_at[i] = True
                return True

            if nums[i] == 0:
                can_jump_at[i] = False
                return False

            for j in range(1, nums[i] + 1):
                if can_jump_recursive_memoize(i + j):
                    can_jump_at[i] = True
                    return True

            can_jump_at[i] = False
            return False

        return can_jump_recursive_memoize(0)

sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([2,0,0]))
