class KMP:
    def search(self, text, pattern):
        if not text or not pattern or len(pattern) > len(text):
            return None
        dfa = self._construct_dfa(pattern)
        N, M = len(text), len(pattern)
        state = 0
        for i in range(N):
            state = dfa[ord(text[i])][state]
            if state == M:
                return i - M + 1
        return N

    def _construct_dfa(self, pattern):
        if not pattern: return None
        R, M = 256, len(pattern)
        dfa = [[0 for _ in range(M)] for _ in range(R)]
        prev_state = 0
        
        dfa[ord(pattern[0])][0] = 1
        for j in range(1, M):
            for c in range(R):
                dfa[c][j] = dfa[c][prev_state]
            dfa[ord(pattern[j])][j] = j + 1
            prev_state = dfa[ord(pattern[j])][prev_state]
        
        assert prev_state == 0
        return dfa

class BoyerMoore:
    def search(self, text, pattern):
        if not text or not pattern: return None

        N, M = len(text), len(pattern) 
        i = 0 
        right = self.compute_rightmost_index(pattern)

        while i <= N - M:
            skip = 0
            for j in range(M - 1, -1, -1):
                if text[i + j] != pattern[j]:
                    mismatch_char = text[i + j]
                    if right[ord(mismatch_char)] == -1:
                        skip = j + 1
                    else:
                        if right[ord(mismatch_char)] > j:
                            skip = 1
                        else:
                            skip = right[ord(mismatch_char)] + j
            if skip == 0: 
                return i
            i += skip

        return N

    def compute_rightmost_index(self, pattern):
        table = [-1] * 128
        for i in range(len(pattern)):
            table[ord(pattern[i])] = i
        return table

class RabinKarp():
    def hash_text(self, text, N):
        if not text or N <= 0:
            return None
        text_hash, R, Q = 0, 256, 993
        for i in range(N):
            text_hash = (text_hash * R + ord(text[i])) % Q
        return text_hash
    
    def search(self, text, pattern):
        if not text or not pattern or len(text) < len(pattern):
            return None

        R, Q, M, N = 256, 993, len(pattern), len(text)
        RM  = 256 ** (M - 1)
        pattern_hash = self.hash_text(pattern, M)
        text_hash = self.hash_text(text, M)
        if pattern_hash == text_hash: return 0

        for i in range(M, N):
            text_hash = (text_hash + Q - (ord(text[i-M]) * RM % Q)) % Q
            text_hash = (text_hash * R + ord(text[i])) % Q
            if text_hash == pattern_hash:
                return i - M + 1
        return N

kmp = KMP()
bm = BoyerMoore()
rk = RabinKarp()

print('Knuth-Morris-Pratt: Expect 6: {}'.format(kmp.search('AABACAABABACAA', 'ABABAC')))
print('Boyer-Moore: Expect 6: {}'.format(bm.search('AABACAABABACAA', 'ABABAC')))
print('Rabin-Karp: Expect 6: {}'.format(rk.search('AABACAABABACAA', 'ABABAC')))

print('Knuth-Morris-Pratt: Expect 15: {}'.format(kmp.search('FINDINAHAYSTACKNEEDLEINA', 'NEEDLE')))
print('Boyer-Moore: Expect 15: {}'.format(bm.search('FINDINAHAYSTACKNEEDLEINA', 'NEEDLE')))
print('Rabin-Karp: Expect 15: {}'.format(rk.search('FINDINAHAYSTACKNEEDLEINA', 'NEEDLE')))
