class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_cols = set()
        seen_rows = set()

        box = [set() for _ in range(3)]
        for i in range (9):
            if i%3 == 0:
                print('Box: ', box)
                box = [set() for _ in range(3)]

            for j in range (9):
                # columns
                if board[i][j] != ".":
                    if board[i][j] in seen_cols:
                        return False
                    seen_cols.add(board[i][j])
                    # box 3x3
                    if board[i][j] in box[j//3]:
                        return False
                    box[j//3].add(board[i][j])
                   
                # rows
                if board[j][i] != ".":
                    if board[j][i] in seen_rows:
                        return False
                    seen_rows.add(board[j][i])
                    
            seen_cols = set()
            seen_rows = set()
        return True
        