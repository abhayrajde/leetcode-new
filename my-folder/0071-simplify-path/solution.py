class Solution:
    def simplifyPath(self, path: str) -> str:
        # use stack, create parts using split
        # if part is empty or part is '.': continue
        # if part is '..', pop from stack
        # else append to stack and later join using '/' 
        stack = []
        parts = path.split('/')
        for part in parts:
            if part != '' and part != '.':
                if part == '..':
                    if len(stack) != 0:
                        stack.pop()
                else:
                    stack.append(part)

        return '/' + '/'.join(stack)

            
