class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element == '+':
                stack.append(stack.pop() + stack.pop())
            elif element == '-':
                secondEl, firstEl = stack.pop(), stack.pop()
                stack.append(firstEl - secondEl)
            elif element == '*':
                stack.append(stack.pop() * stack.pop())
            elif element == '/':
                secondEl, firstEl = stack.pop(), stack.pop()
                stack.append(int(firstEl / secondEl))
            else:
                stack.append(int(element))
        return stack[0]
