'''

'''
from collections import deque

def getShiftedString(s, leftShifts, rightShifts):
    text = deque(s)
    text.rotate(-leftShifts)
    text.rotate(rightShifts)
    return ''.join(text)


print(getShiftedString('abcd', 1, 2))
print(getShiftedString('a', 0, 1))
