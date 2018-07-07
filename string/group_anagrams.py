'''
https://leetcode.com/problems/group-anagrams/description/
'''

from collections import defaultdict
import math

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        return self.group_anagrams_prime(strs)

    def group_anagrams_sort(self, strs):
        anagram_words = defaultdict(list)
        for word in strs:
            anagram_words[''.join(sorted(word))].append(word)
        return [anagram_words[word] for word in anagram_words]

    def group_anagrams_prime(self, strs):
        primes = self.generate_primes_less_than(103)
        assert len(primes) == 26
        groups = defaultdict(list)

        for word in strs:
            prime_hash = 1
            for c in word:
                prime_hash *= primes[ord(c) - ord('a')]
            groups[prime_hash].append(word)

        return [groups[anagram] for anagram in groups]

    def generate_primes_less_than(self, n):
        prime_numbers = [True] * n
        for i in range(2, int(math.sqrt(n))):
            if prime_numbers[i] == True:
                for j in range(i+i, n, i):
                    prime_numbers[j] = False
        return [x for x in range(2,n) if prime_numbers[x]]

sol = Solution()
print(sol.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
