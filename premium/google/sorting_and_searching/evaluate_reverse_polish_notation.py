import math
class Solution:
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token == '/' or token == '*' or token == '+' or token == '-':
                b, a = stack.pop(), stack.pop()
                stack.append(self.eval(a, b, token))
            else:
                stack.append(int(token))
        return stack[-1]

    def eval(self, a, b, op):
        a, b = int(a), int(b)
        if op == '/':
            return math.ceil(a / b) if a / b < 0 else math.floor(a / b)
        elif op == '*':
            return a * b
        elif op == '+':
            return a + b
        elif op == '-':
            return a - b
        else:
            raise Error('unexpected operator: {}'.format(op))

sol = Solution()
res = sol.evalRPN(['1','5','+'])
print(res)
res2 = sol.evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
print(res2)
res3 = sol.evalRPN(['4','-2','/','2','-3','-','-'])
print(res3)
