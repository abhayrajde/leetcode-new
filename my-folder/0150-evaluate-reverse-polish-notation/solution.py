class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def __init__(self):
        self.operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }

    def evalRPN(self, tokens):
        if not tokens:
            return 0

        stack = []

        for token in tokens:
            if token in self.operators:
                stack.append(self.operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[0]
# class Solution(object):
#     def evalRPN(self, tokens):
#         stack = []
#         for i in tokens:
#             if i == '+':
#                 d2 = stack.pop()
#                 d1 = stack.pop()
#                 stack.append(d1 + d2)
#             elif i == '-':
#                 d2 = stack.pop()
#                 d1 = stack.pop()
#                 stack.append(d1 - d2)
#             elif i == '*':
#                 d2 = stack.pop()
#                 d1 = stack.pop()
#                 stack.append(d1 * d2)
#             elif i == '/':
#                 d2 = stack.pop()
#                 d1 = stack.pop()
#                 stack.append(int(d1 / d2))
#             else:
#                 stack.append(int(i))
#         return stack[0]
#         """
#         :type tokens: List[str]
#         :rtype: int
#         """
        
