'''
https://leetcode.com/explore/interview/card/google/67/sql-2/472/
'''
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if K <= 0 or K > len(S): None
        num_in_group = 0
        res = []
        for i in range(len(S) - 1, -1, -1):
            if num_in_group == K and S[i] != '-':
                res.append('-')
                num_in_group = 0

            if S[i] != '-':
                if '0' <= S[i] <= '9':
                    res.append(S[i])
                else:
                    res.append(S[i].upper())
                num_in_group += 1
        
        return ''.join(res[::-1])
    
    def license_key_formatting(self, s, k):
        res = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] != '-':
                if len(res) % (k + 1) == k:
                    res.append('-')
                res.append(s[i])
        
        return ''.join(res[::-1]).upper()

sol = Solution()
S = '5F3Z-2e-9-w'
S2 = '2-5g-3-J'

print(sol.licenseKeyFormatting(S, 4))
print(sol.licenseKeyFormatting(S2, 2))
print(sol.license_key_formatting(S, 4))
print(sol.license_key_formatting(S2, 2))
