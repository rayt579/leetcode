'''
https://leetcode.com/problems/encode-and-decode-strings/description/
'''

class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        encoded_str = []
        for word in strs:
            encoded_str.append(str(len(word)))
            encoded_str.append('/')
            encoded_str.append(word)
        return ''.join(encoded_str)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        words = []
        i = 0
        while i < len(s):
            slash_index = s.find('/', i)
            size = int(s[i:slash_index])
            words.append(s[slash_index + 1:slash_index + 1 + size])
            i =  slash_index + size + 1
        return words



# Your Codec object will be instantiated and called as such:
codec = Codec()
strs = ['cat', 'dog','puppy']
print(codec.decode(codec.encode(strs)))
