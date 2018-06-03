def number_decodings(s):
    return 0 if not s else num_decodings(0, s)

def num_decodings(p, s):
    n = len(s)
    if p == n: return 1
    if s[p] == '0': return 0
    res = num_decodings(p + 1, s)
    if p < n - 1 and (s[p] == '1' or (s[p] == '2' and s[p + 1] < '7')):
        res += num_decodings(p + 2, s)
    return res

a = '12'
b = '226'
print('Expect 2: {}'.format(number_decodings(a)))
print('Expect 3: {}'.format(number_decodings(b)))

