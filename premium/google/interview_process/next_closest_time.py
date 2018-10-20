'''
https://leetcode.com/explore/interview/card/google/67/sql-2/471/
'''

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """ 
        digits = list(time)
        digits.remove(':') 
        digits = list(map(int, digits))

        original_digits = [False] * 10
        for digit in digits:
            original_digits[int(digit)] = True
        
        while True:
            digits[3] = (digits[3] + 1) % 10
            if digits[3] == 0:
                digits[2] = (digits[2] + 1) % 6
                if digits[2] == 0:
                    digits[1] = (digits[1] + 1) % 4 if digits[0] == 2 else (digits[1] + 1) % 10
                    if digits[1] == 0:
                        digits[0] = (digits[0] + 1) % 3
            
            for i in range(len(digits)):
                if not original_digits[digits[i]]:
                    break
                if i == len(digits) - 1:
                    digits = list(map(str, digits))
                    digits.insert(2,':')
                    return ''.join(digits)

           
sol = Solution()
#print('Expect 19:29: {}'.format(sol.nextClosestTime('19:24')))
print('Expect 22:22 {}'.format(sol.nextClosestTime('23:59')))
