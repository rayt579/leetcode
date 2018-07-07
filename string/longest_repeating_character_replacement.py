'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''

class Solution(object):
    def characterReplacement(self, s, k):
        return self.character_replacement_sliding(s, k)

    def character_replacement_math(self, s, k):
        count = [0] * 26
        max_count = 0
        start = 0
        for end in range(len(s)):
            count[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[end]) - ord('A')])
            if max_count + k <= end - start:
                count[ord(s[start]) - ord('A')] -= 1
                start += 1
        return len(s) - start

    def character_replacement_sliding(self, s, k):
        start, max_count, max_length = 0, 0, 0
        counts = [0] * 26
        for end in range(len(s)):
            counts[ord(s[end]) - ord('A')] += 1
            max_count = max(max_count, counts[ord(s[end]) - ord('A')])
            if end - start + 1 - max_count > k:
                counts[ord(s[start]) - ord('A')] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length

    def characterReplacement_inefficient(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        letters = set(s)
        for letter in letters:
            for start in range(len(s)):
                tol = k
                for curr in range(start, len(s)):
                    if s[curr] != letter:
                        if tol == 0:
                            max_length = max(max_length, curr - start)
                            break
                        else:
                            tol -= 1
                            max_length = max(max_length, curr - start + 1)
                    else:
                        max_length = max(max_length, curr - start + 1)

        return max_length

sol = Solution()
print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))
print(sol.characterReplacement("AAAA", 2))
