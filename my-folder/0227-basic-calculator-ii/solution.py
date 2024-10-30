class Solution:
    def calculate(self, s: str) -> int:
        # taking a stack and putting in the number if we get operation of + or -, 
        # but if we got * or / we directly caluclate them with this operator, 
        # at the end caluclate the sum of stack is answer

        stack = []
        prev_operator = "+"
        curr_num = 0

        for i in range(len(s)):

            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i]) # what if we have double or triple digits
            
            if s[i] in "+-*/" or i == len(s) - 1:

                if prev_operator == "+":
                    stack.append(curr_num)
                if prev_operator == "-":
                    stack.append(-curr_num)
                if prev_operator == "*":
                    stack[-1] = stack[-1] * curr_num
                if prev_operator == "/":
                    stack[-1] = int(stack[-1] / curr_num) # don't use stack[-1]//curr_num it will give -5/2 to -3 but we want -2 so we use int, as it will remove anything after "." by giving -2

                prev_operator = s[i]
                curr_num = 0
        
        return sum(stack)

