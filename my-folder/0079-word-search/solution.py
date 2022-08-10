class Solution(object):
    def exist(self, board, word):
        path = set()
        
        rows, cols = len(board), len(board[0])
        def backtrack(i,r,c):
            if(i == len(word)):
                return True
            if((r,c) in path or r< 0 or c < 0 or r >=rows or c >= cols or board[r][c] != word[i]):
                return False
            
            path.add((r,c))
            
            res = (backtrack(i+1,r+1,c) or backtrack(i+1,r,c+1) or backtrack(i+1,r-1,c) or backtrack(i+1,r,c-1))
            
            path.remove((r,c))
            return(res)
        
        for r in range(rows):
            for c in range(cols):
                if(board[r][c] == word[0] and backtrack(0,r,c)):
                    return True
        return False
                
        
            
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
