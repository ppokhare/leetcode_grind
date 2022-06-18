class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        #idea2: same as idea 1  but using dict of set for all row, col, subBox. 
        #Runtime: O(n^2) instead of O(3*n^2). and Sapce: O(3*n^2) instand of O(n+n+n^2)
        row = defaultdict(set)
        col = defaultdict(set)
        subBox = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    if(board[r][c] in row[r] or 
                       board[r][c] in col[c] or 
                       board[r][c] in subBox[(r/3, c/3)]): return False
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    subBox[(r/3,c/3)].add(board[r][c])
        return True
                     
        
#         #idea1:
#         #checking row digits
#         for i in range(9):
#             rowSet = set()
#             for j in range(9):
#                 if board[i][j]!= '.':
#                     if board[i][j] in rowSet: return False
#                     rowSet.add(board[i][j])
        
#         #checking column digits
#         for i in range(9):
#             colSet = set()
#             for j in range(9):
#                 if board[j][i] != '.':
#                     if board[j][i] in colSet: return False
#                     colSet.add(board[j][i])
         
#         #checking 3x3 sub-boxes
#         subBox = defaultdict(set)
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j] != '.':
#                     if board[i][j] in subBox[(i/3,j/3)]: return False
#                     else: subBox[(i/3,j/3)].add(board[i][j])
#         return True