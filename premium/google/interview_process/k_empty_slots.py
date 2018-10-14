'''
https://leetcode.com/explore/interview/card/google/67/sql-2/470/
'''

class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers or k < 0: return -1
        N = len(flowers)
        bloomed = [False] * (N + 1)
        for i in range(N):
            curr = flowers[i]
            left = flowers[i] - 1 - k
            right = flowers[i] + 1 + k
            
            bloomed[curr] = True

            if 0 <= left <= N and bloomed[left]:
                j = left + 1
                while 0 <= j < curr and not bloomed[j]:
                    j += 1
                if j == curr or k == 0:
                    return i + 1

            if 0 <= right <= N and bloomed[right]:
                j = right - 1
                while curr < j <= N and not bloomed[j]:
                    j -= 1
                if j == curr or k == 0:
                    return i + 1

        return -1

sol = Solution()
print('Expecting 2: {}'.format(sol.kEmptySlots([1,3,2], 1)))
print('Expecting -1: {}'.format(sol.kEmptySlots([1,2,3], 1)))
print('Expecting 2: {}'.format(sol.kEmptySlots([10,1,9,3,5,7,6,4,8,2], 8)))
