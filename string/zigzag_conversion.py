'''
https://leetcode.com/problems/zigzag-conversion/description/
'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0:
            raise ValueError('Need at > 0 number of rows')
        if numRows == 1:
            return s
        buckets = [[] for _ in range(numRows)]
        bucket_index, direction = 0, -1
        for i in range(len(s)):
            buckets[bucket_index].append(s[i])
            if bucket_index == 0 or bucket_index == numRows - 1:
                direction = -direction
            bucket_index += direction

        return ''.join([''.join(bucket) for bucket in buckets])

sol = Solution()
s = 'PAYPALISHIRING'
print('Expecting PAYPALISHIRING: {}'.format(sol.convert(s, 1)))
print('Expecting PYAIHRNAPLSIIG: {}'.format(sol.convert(s, 2)))
print('Expecting PAHNAPLSIIGYIR: {}'.format(sol.convert(s, 3)))
print('Expecting PINALSIGYAHRPI: {}'.format(sol.convert(s, 4)))