'''
https://leetcode.com/problems/group-anagrams/description/
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_words = defaultdict(list)
        for word in strs:
            anagram_words[''.join(sorted(word))].append(word)
        return [anagram_words[word] for word in anagram_words]

sol = Solution()
print(sol.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
