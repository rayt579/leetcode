#https://leetcode.com/problems/read-n-characters-given-read4/

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        start = 0
        buf4 = ['','','','']

        while start < n:
            chars_read_from_buffer = read4(buf4)
            if chars_read_from_buffer == 0: break
            
            chars_left_to_read = n - start
            chars_to_copy = min(chars_read_from_buffer, chars_left_to_read)
            buf[start:start + chars_to_copy] = buf4[:chars_to_copy]
            start += chars_to_copy
        return start
