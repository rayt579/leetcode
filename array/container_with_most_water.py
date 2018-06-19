class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def max_area_brute_force(self, height):
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                max_area = max(max_area, (j - i) * min(height[i], height[j]))
        return max_area

sol = Solution()

all_duplicates = [5,5,5,5,5]
sorted_heights_ascending = [1, 2, 3]
sorted_heights_descending = [3,2,1]


print('Expect 20: {}'.format(sol.maxArea(all_duplicates)))
print('Expect 2: {}'.format(sol.maxArea(sorted_heights_ascending)))
print('Expect 2: {}'.format(sol.maxArea(sorted_heights_descending)))
