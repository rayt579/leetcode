'''
https://leetcode.com/explore/interview/card/google/62/recursion-4/399/
'''
class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def find_strobogrammatic(n, m):
            if n == 0:
                return ['']
            if n == 1:
                return ['0','1','8']
            
            strobo, prev_strobo = [], []
            prev_strobo += find_strobogrammatic(n - 2, m)
            for num in prev_strobo:
                if n != m:
                    strobo.append('0' + num + '0')
                strobo.append('1' + num + '1')
                strobo.append('6' + num + '9')
                strobo.append('8' + num + '8')
                strobo.append('9' + num + '6')
            
            return strobo
        
        return find_strobogrammatic(n, n)

sol = Solution()
print('for n = 1: {}'.format(sol.findStrobogrammatic(1)))
print('for n = 2: {}'.format(sol.findStrobogrammatic(2)))
print('for n = 3: {}'.format(sol.findStrobogrammatic(3)))
