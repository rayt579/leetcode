'''
https://leetcode.com/explore/interview/card/amazon/81/design/896/
'''
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['end'] = 'end'


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        return 'end' in curr


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True



# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert('apple')
print('Expect True: {}'.format(trie.search('apple')))
print('Expect False: {}'.format(trie.search('app')))
print('Expect True: {}'.format(trie.startsWith('app')))
trie.insert('app')
print('Expect True: {}'.format(trie.search('app')))
