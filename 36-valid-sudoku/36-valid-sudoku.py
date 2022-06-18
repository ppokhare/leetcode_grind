class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #checking row digits
        for i in range(9):
            rowSet = set()
            for j in range(9):
                if board[i][j]!= '.':
                    if board[i][j] in rowSet: return False
                    rowSet.add(board[i][j])
        
        #checking column digits
        for i in range(9):
            colSet = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in colSet: return False
                    colSet.add(board[j][i])
         
        #checking 3x3 sub-boxes
        subBox = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in subBox[(i/3,j/3)]: return False
                    else: subBox[(i/3,j/3)].add(board[i][j])
        return True