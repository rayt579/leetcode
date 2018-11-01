'''
https://leetcode.com/explore/interview/card/google/67/sql-2/469
'''

class Solution:
    def repeatedStringMatch(self, A, B):
        return self.repeated_string_match_kmp_space_optimized(A, B)

    def repeated_string_match_simulated(self, A, B):
        if not A or not B:
            return -1
        count = 0
        sb = []
        while len(sb) < len(B):
            sb.extend(list(A))
            count += 1
        if B in ''.join(sb):
            return count
        sb.extend(list(A))
        count += 1

        return count if B in ''.join(sb) else -1

    def repeated_string_match_rolling(self, A, B):
        if not A or not B:
            return -1

        M, N = len(A), len(B)
        for i in range(M):
            j = 0 
            while j < N and A[(i + j) % M] == B[j]: 
                j += 1
            if j == N:
                offset = 1 if (i + j) % M != 0 else 0
                return (i + j) // M + offset
        return -1

    def repeated_string_match_clever(self, A, B):
        if not A or not B: return -1

        m, n = len(A), len(B)
        cycles = -(-n // m) #calculate ceiling
        for i in range(2):
            if B in A * (cycles + i):
                return cycles + i
        return -1

    def repeated_string_match_kmp_space_optimized(self, A, B):
        def construct_prefix_table(pattern):
            M = len(pattern)
            pref_table = [0] * (M + 1)
            pp, sp = 0, 1
            while sp < M:
                if pattern[pp] == pattern[sp]:
                    pp += 1
                    sp += 1
                    pref_table[sp] = pp
                elif pp == 0:
                    sp += 1
                    pref_table[sp] = 0
                else:
                    pp = pref_table[pp]
            
            return pref_table
        
        if not A or not B:
            return -1

        M, N = len(A), len(B)
        pref_table = construct_prefix_table(B)
        i, j = 0, 0
        while i < M:
            while j < N and A[(i + j) % M] == B[j]:
                j += 1
            if j == N:
                offset = 0 if (i + j) % M == 0 else 1
                return (i + j)//M + offset
            
            i += max(1, j - pref_table[j])
            j = pref_table[j]

        return -1


sol = Solution()
print('Expecting 3: {}'.format(sol.repeatedStringMatch('abcd', 'cdabcdab')))
