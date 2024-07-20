class Solution(object):
    def isValidSudoku(self, board):
        rowhm = defaultdict(set)
        colhm = defaultdict(set)
        cubehm = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if(board[r][c] != "."):
                    x = r/3
                    y = c/3
                    if(board[r][c] in rowhm[r] or board[r][c] in colhm[c] or board[r][c] in cubehm[(x,y)]):
                        return False
                    rowhm[r].add(board[r][c])
                    colhm[c].add(board[r][c])
                    cubehm[(x,y)].add(board[r][c])         
        return True
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
