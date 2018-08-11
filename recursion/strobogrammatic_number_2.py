'''
https://leetcode.com/problems/strobogrammatic-number-ii/description/
'''

class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(n, m):
            if n == 0:
                return ['']
            if n == 1:
                return ['0', '1', '8']
            numbers = helper(n - 2, m)
            results = []
            for i in range(len(numbers)):
                if n != m:
                    results.append('0' + numbers[i] + '0')
                results.append('1' + numbers[i] + '1')
                results.append('8' + numbers[i] + '8')
                results.append('6' + numbers[i] + '9')
                results.append('9' + numbers[i] + '6')
            return results

        return helper(n, n)

sol = Solution()
print('n = 1: {}'.format(sol.findStrobogrammatic(1)))
print('n = 2: {}'.format(sol.findStrobogrammatic(2)))
print('n = 3: {}'.format(sol.findStrobogrammatic(3)))
print('n = 4: {}'.format(sol.findStrobogrammatic(4)))
