'''
https://leetcode.com/problems/implement-trie-prefix-tree/description/
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
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node['end_word'] = None


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return 'end_word' in current_node


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for letter in prefix:	
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return True

# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('cat')
obj.insert('cats')
obj.insert('dog')
print('Found cat: {}'.format(obj.search('cat')))
print('Found cats: {}'.format(obj.search('cats')))
print('Found dog: {}'.format(obj.search('dog')))
print('Found catalysis: {}'.format(obj.search('catalysis')))

# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
