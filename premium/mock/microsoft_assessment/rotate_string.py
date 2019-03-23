from collections import deque
#Time O(n^2) time, O(n^2) space for allocating the buffer.
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return self.rotate_string_efficient(A, B)

    def rotate_string_straightforward(self, A, B):
        if len(A) != len(B):
            return False
       
        num_rotations, n = 0, len(A)
        string_buffer = deque(list(A))
        
        while num_rotations < n:
            str_a = ''.join(string_buffer)
            if str_a == B:
                return True
            string_buffer.append(string_buffer.popleft())
            num_rotations += 1
        return False if A != B else True

    def rotate_string_efficient(self, A, B):
        return B in A + A if len(A) == len(B) else False

sol = Solution()
print('Expecting True: {}'.format(sol.rotateString('abcde', 'cdeab')))
