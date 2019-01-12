class TrieNode:
    def __init__(self):
        self.words = []
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def create_trie_from_words(self, words):
        for word in words:
            curr = self.root
            for ch in word:
                idx = ord(ch) - ord('a')
                if not curr.children[idx]:
                    curr.children[idx] = TrieNode()
                curr.children[idx].words.append(word)
                curr = curr.children[idx]

    def find_words_for_prefix(self, prefix):
        curr = self.root
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not curr.children[idx]:
                return []
            curr = curr.children[idx]
        return curr.words

class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        word_squares, curr_square = [], []
        trie = Trie()
        trie.create_trie_from_words(words)
        for word in words:
            curr_square.append(word)
            self.backtrack(curr_square, trie, word_squares)
            curr_square.pop()
        return word_squares

    def backtrack(self, curr_square, trie, word_squares):
        if len(curr_square) == len(curr_square[0]):
            word_squares.append(list(curr_square))
            return
        prefix = ''.join([word[len(curr_square)] for word in curr_square])
        word_matches = trie.find_words_for_prefix(prefix)
        for word in word_matches:
            curr_square.append(word)
            self.backtrack(curr_square, trie, word_squares)
            curr_square.pop()

sol = Solution()
res = sol.wordSquares(['area','lead','wall','lady','ball'])
print(res)
