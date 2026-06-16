class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recurse(row, col, pos):
            # boundaries
            if 0>row or row>=len(board) or 0>col or col>=len(board[0]):
                return False
            # visited
            if (row, col) in visited:
                return False
            #no match
            if board[row][col] != word[pos]:
                return False
            visited.add((row, col))
            pos += 1
            if pos == len(word):
                return True
            if recurse(row+1, col, pos) or recurse(row-1, col, pos) or recurse(row, col+1, pos) or recurse(row, col-1, pos):
                return True
            visited.remove((row, col))
            return False



        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if recurse(i,j,0):
                    return True

        return False

        