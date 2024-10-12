class Solution:
    def simplifyPath(self, path: str) -> str:
        output = []
        parts = path.split('/')
        for part in parts:
            if part != '' and part != '.':
                if part == '..':
                    if len(output) != 0:
                        output.pop()
                else:
                    output.append(part)

        return '/' + '/'.join(output)

            
