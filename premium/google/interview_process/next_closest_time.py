'''
https://leetcode.com/explore/interview/card/google/67/sql-2/471/
'''

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """ 
        numbers = sorted(time[0:2] + time[3:])
        time = list(time)
        for i in range(len(numbers)):
            if numbers[i] > time[4]:
                time[4] = numbers[i]
                return ''.join(time)

        for i in range(len(numbers)):
            if numbers[i] > time[3] and '0' <= numbers[i] <= '5':
                time[3] = numbers[i]
                time[4] = numbers[i]
                return ''.join(time)

        if time[0] == 2:
            for i in range(len(numbers)):
                if numbers[i] > time[1] and '0' <= numbers[i] <= '3':
                    time[1] = numbers[i]
                    time[3] = numbers[i]
                    time[4] = numbers[i]
                    return ''.join(time)
        else:
            for i in range(len(numbers)):
                if numbers[i] > time[1] and '0' <= numbers[i] <= '9':
                    time[1] = numbers[i]
                    time[3] = numbers[i]
                    time[4] = numbers[i]
                    return ''.join(time)
        
        time[1] = numbers[0]
        time[3] = numbers[0]
        time[4] = numbers[0]
        return ''.join(time)

sol = Solution()
print('Expect 11:11: {}'.format(sol.nextClosestTime('19:49')))
print('Expect 19:29: {}'.format(sol.nextClosestTime('19:24')))
print('Expect 04:44: {}'.format(sol.nextClosestTime('04:29')))
print('Expect 15:55 {}'.format(sol.nextClosestTime('12:59')))
print('Expect 22:22 {}'.format(sol.nextClosestTime('23:59')))
