class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend_palindrome(i, j):
            start, end = 0, 0
            while i >= 0 and j < len(s) and s[i] == s[j]:
                start, end = i, j
                i -= 1
                j += 1
            return (start, end)

        longest_palindrome_length = 0
        lp_start = 0
        if not s or len(s) == 0:
            return ''
        for i in range(len(s) - 1):
            c1_start, c1_end = extend_palindrome(i, i)
            c2_start, c2_end = extend_palindrome(i, i + 1)
            length_c1, length_c2 = c1_end - c1_start + 1, c2_end - c2_start + 1
            
            length = max(length_c1, length_c2)
            if length > longest_palindrome_length:
                longest_palindrome_length = length
                if length == length_c1:
                    lp_start = c1_start
                else:
                    lp_start = c2_start

        return s[lp_start:lp_start + longest_palindrome_length] if len(s) > 1 else s[0]

sol = Solution()
s1 = 'babad'
s2 = 'cbbd'
s3 = 'a'
print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))
print(sol.longestPalindrome(s3))
