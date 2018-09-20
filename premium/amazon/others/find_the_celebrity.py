'''
https://leetcode.com/explore/interview/card/amazon/82/others/893/
'''

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, n - 1
        while a < b:
            if knows(a, b):
                a += 1
            else:
                b -= 1
        for i in range(n):
            if i != a and (not knows(i, a) or knows(a, i)):
                return -1
        return a



