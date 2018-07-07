'''
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n, A, B = len(nums1), len(nums2), nums1, nums2
        if m > n:
            m, n, A, B = n, m, B, A

        lo, hi = 0, m
        while lo <= hi:
            i = (hi - lo)//2 + lo
            j = (m + n)//2 - i
            if i < m and B[j-1] > A[i]:
                lo = i + 1
            elif i > 0 and A[i-1] > B[j]:
                hi = i - 1
            else:
                if i == 0:
                    max_left = B[j-1]
                elif j == 0:
                    max_left = A[i-1]
                else:
                    max_left = max(A[i-1], B[j-1])

                if i == m:
                    min_right = B[j]
                elif j == n:
                    min_right = A[i]
                else:
                    min_right = min(A[i], B[j])

                if (m + n) % 2 == 1:
                    if i + j > m - i + n - j:
                        return float(max_left)
                    else:
                        return float(min_right)

                return (max_left + min_right) / 2.0


sol = Solution()
a = [1,2]
b = [3,4]
a_1 = [1,3]
b_1 = [2]

print('Expecting 2.5: {}'.format(sol.findMedianSortedArrays(a, b)))
print('Expecting 2.0: {}'.format(sol.findMedianSortedArrays(a_1, b_1)))


