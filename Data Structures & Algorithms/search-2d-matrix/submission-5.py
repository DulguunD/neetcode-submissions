class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_lower = 0
        row_higher = len(matrix)-1

        col_lower = 0
        col_higher = len(matrix[0])-1

        while row_lower <= row_higher:
            row = int((row_lower+row_higher)/2)
            # col = int((col_lower+col_higher)/2)
            # print(f"row_lower: {row_lower}, higher: {row_higher}, row: {row}")
            if matrix[row][0] <= target:
                # print(f"Value: {matrix[row][0]}, Target: {target}")
                # print(f"Might Found: {matrix[row][0]}, row: {row}")
                # break
                if row+1 < len(matrix) and matrix[row+1][0] > target:
                    break
                row_lower = row+1
                # continue
            elif matrix[row][0] > target:
                row_higher = row-1
                # continue
            # else:
            #     break
            #     # print(f"row_lower: {row_lower}, higher: {row_higher}")
            #     print(f"Found row: {row}")
            #     return True     
          
        # print(f"Final Found: {matrix[row][0]}, row: {row}")

        while row < len(matrix) and col_lower <= col_higher:
            col = int((col_lower+col_higher)/2)
            # print(f"col: {col}, col_lower: {col_lower}, col_higher: {col_higher}")
            if matrix[row][col] < target:
                col_lower = col+1
                # continue
            elif matrix[row][col] > target:
                col_higher = col-1
            else:
                # print(f"\tFound {matrix[row][col]}")
                return True





        return False
        