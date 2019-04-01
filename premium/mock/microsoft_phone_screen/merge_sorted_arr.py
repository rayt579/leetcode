class Solution:
    def merge(self, nums1, m, nums2 , n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        return self.merge_optimize_space(nums1, m, nums2, n)

    # O(m + n) time, O(1) space
    def merge_optimize_space(self, nums1, m, nums2, n):
        i, j, k = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

    '''
    Time: O(m + n) time, two pass solution
    Space: O(m + n) space, allocating a swap array
    '''
    def merge_straightforward(self, nums1, m, nums2, n):
        merged = []
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if i == m:
            while j < n:
                merged.append(nums2[j])
                j += 1
        elif j == n:
            while i < m:
                merged.append(nums1[i])
                i += 1

        for k in range(m + n):
            nums1[k] = merged[k]


sol = Solution()
nums1 = [1,2,3,0,0,0]
nums2 = [2, 5, 6]
print('Before: {}'.format(nums1))
print('Before: {}'.format(nums2))
sol.merge(nums1, 3, nums2, 3)
print('After: {}'.format(nums1))
