class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        return self.compare_versions_using_pointer_comparison(version1, version2)

    def compare_versions_using_pointer_comparison(self, version1, version2):
        m, n = len(version1), len(version2)
        i, j = 0, 0
        num1, num2 = 0, 0
        while i < m or i < n:
            while i < m and version1[i] != '.':
                num1 += (10 * num1) + int(version1[i])
                i += 1
            while j < n and version2[j] != '.':
                num2 += (10 * num2) + int(version2[j])
                j += 1
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                i += 1
                j += 1
                num1, num2 = 0, 0
        return 0
    
    def compare_versions_using_split(self, version1, version2):
        digits_v1, digits_v2 = version1.split('.'), version2.split('.')
        length = max(len(digits_v1), len(digits_v2))
        i = 0
        for i in range(length):
            num_at_level_v1 = int(digits_v1[i]) if i < len(digits_v1) else 0
            num_at_level_v2 = int(digits_v2[i]) if i < len(digits_v2) else 0
            if num_at_level_v1 < num_at_level_v2:
                return -1
            elif num_at_level_v2 < num_at_level_v1:
                return 1
        return 0

sol = Solution()
print('Expecting result -1: {}'.format(sol.compareVersion('0.1', '1.1')))
print('Expecting result 1: {}'.format(sol.compareVersion('1.0.1', '1')))
print('Expecting result -1: {}'.format(sol.compareVersion('7.5.2.4', '7.5.3')))
