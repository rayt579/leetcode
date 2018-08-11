'''
https://leetcode.com/explore/interview/card/amazon/76/array-and-strings/502
'''

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        return self.compare_version(version1, version2)

    def compare_version(self, v1, v2):
        m, n = len(v1), len(v2)
        i, j = 0, 0

        num1, num2 = 0, 0
        while i < m or j < n:
            while i < m and v1[i] != '.':
                num1 = (10 * num1) + ord(v1[i]) - ord('0')
                i += 1
            while j < n and v2[j] != '.':
                num2 = (10 * num2) + ord(v2[j]) - ord('0')
                j += 1
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                num1 = 0
                num2 = 0
                i += 1
                j += 1
        return 0


sol = Solution()
print('Expect -1: {}'.format(sol.compareVersion('0.1','1.1')))
print('Expect 1: {}'.format(sol.compareVersion('1.0.1','1')))
print('Expect -1: {}'.format(sol.compareVersion('7.5.2.4','7.5.3')))
