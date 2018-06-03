'''
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
'''
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        if word is None:
            return
        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        curr['end_of_word'] = None

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.match(word, 0, self.root)

    def match(self, chs, i, node):
        if i == len(chs):
            return 'end_of_word' in node
        if chs[i] != '.':
            return chs[i] in node and self.match(chs, i + 1, node[chs[i]])
        else:
            for child in node:
                if child != 'end_of_word':
                    if self.match(chs, i + 1, node[child]):
                        return True
        return False

# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("cat")
obj.addWord("dog")

print('Expecting true: {}'.format(obj.search("cat")))
print('Expecting true: {}'.format(obj.search("dog")))
print('Expecting true: {}'.format(obj.search(".og")))
print('Expecting true: {}'.format(obj.search(".o.")))
print('Expecting true: {}'.format(obj.search("...")))

print('Expecting false: {}'.format(obj.search("do")))
print('Expecting false: {}'.format(obj.search("doigg")))
print('Expecting false: {}'.format(obj.search(".")))
print('Expecting false: {}'.format(obj.search("..")))
print('Expecting false: {}'.format(obj.search("....")))


