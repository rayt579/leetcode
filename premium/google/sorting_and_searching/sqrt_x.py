class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        if x == 0 or x == 1:
            return x
        lo, hi = 1, x
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if mid == x // mid:
                return mid
            elif mid < x // mid:
                lo = mid + 1
            else:
                if (mid - 1) < x // (mid - 1):
                    return mid - 1
                hi = mid - 1
        return -1

    def sqrt_bruteforce(self, x):
        num, square = 1, 1
        while square < x:
            num += 1
            square = num * num
        return num if square == x else num - 1

sol = Solution()
print('Expecting 2: {}'.format(sol.mySqrt(4)))
print('Expecting 2: {}'.format(sol.mySqrt(8)))
