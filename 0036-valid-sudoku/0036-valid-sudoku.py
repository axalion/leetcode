class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j]!= ".":
                    seen.add(board[i][j])


        # Check columns
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                elif board[j][i]!= ".":
                    seen.add(board[j][i])


        # Checks squares
        start_pos = [(0,0), (0,3) , (0,6),
                    (3,0), (3,3) , (3,6),
                    (6,0), (6,3) , (6,6)]

        for i,j in start_pos:
            seen = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in seen:
                        return False
                    elif board[row][col]!= ".":
                        seen.add(board[row][col])
        
        return True
                    

        