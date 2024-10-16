class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(path, index):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            possible = mapping[digits[index]]
            for l in possible:
                path.append(l)
                backtrack(path, index + 1)
                path.pop()
            
        combinations = []
        backtrack([], 0)
        return combinations

            

