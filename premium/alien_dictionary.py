'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/510/
'''

from collections import deque, defaultdict
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        neighbors = defaultdict(set)
        indegree = {c:0 for word in words for c in word}

        if not words or len(words) == 0:
            return ''
        if len(words) == 1:
            return words[0]

        for i in range(len(words) - 1):
            curr_word, next_word = words[i], words[i+1]
            length = min(len(curr_word), len(next_word))
            for j in range(length):
                if curr_word[j] != next_word[j]:
                    if next_word[j] not in neighbors[curr_word[j]]:
                        neighbors[curr_word[j]].add(next_word[j])
                        indegree[next_word[j]] += 1
                    break

        visit = deque()
        results = []
        for c in indegree:
            if indegree[c] == 0:
                visit.append(c)
        while len(visit) > 0:
            c = visit.popleft()
            results.append(c)
            for n in neighbors[c]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    visit.append(n)
        return ''.join(results) if len(indegree) == len(results) else ''

sol = Solution()
a = ['wrt', 'wrf', 'er', 'ett', 'rftt']
b = ['z', 'x']
c = ['z', 'x', 'z']
d = ['za','zb','ca','cb']
e = ["bsusz","rhn","gfbrwec","kuw","qvpxbexnhx","gnp","laxutz","qzxccww"]

print('Expecting wertf: {}'.format(sol.alienOrder(a)))
print('Expecting zx: {}'.format(sol.alienOrder(b)))
print('expecting empty: {}'.format(sol.alienOrder(c)))
print('Expecting abzc: {}'.format(sol.alienOrder(d)))
print('Expecting empty: {}'.format(sol.alienOrder(e)))
