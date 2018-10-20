'''
https://leetcode.com/explore/interview/card/google/59/array-and-strings/341/
'''

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0 
        N = len(height)
        left, right = 0, N - 1
        max_left, max_right = 0, 0
        res = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1
        return res

sol = Solution()
print('Expecting 6: {}'.format(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])))
