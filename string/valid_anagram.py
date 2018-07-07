'''
https://leetcode.com/problems/valid-anagram/description/
'''
import math
from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.is_anagram_prime(s, t)

    '''
    This is O(n) time and O(1) space solution
    '''
    def is_anagram_counter(self, s, t):
        return len(Counter(s) - Counter(t)) == 0

    def is_anagram_prime(self, s, t):
        prime_keys = self.generate_primes_less_than(103)
        assert(len(prime_keys) == 26)

        def calculate_prime_hash(text):
            prime_hash = 1
            for c in text:
                prime_hash *= prime_keys[ord(c) - ord('a')]
            return prime_hash

        return calculate_prime_hash(s) == calculate_prime_hash(t)

    def generate_primes_less_than(self, n):
        prime_numbers = [True] * n
        for i in range(2, int(math.sqrt(n))):
            if prime_numbers[i] == True:
                for j in range(i+i, n, i):
                    prime_numbers[j] = False
        return [x for x in range(2,n) if prime_numbers[x]]

sol = Solution()
print('Expect true: {}'.format(sol.isAnagram('anagram','nagaram')))
print('Expect false: {}'.format(sol.isAnagram('rat','car')))
print('----------Prime helper tests----------')
print('Primes less than 108: {}'.format(sol.generate_primes_less_than(108)))
