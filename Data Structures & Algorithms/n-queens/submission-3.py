class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        if n == 1:
            return [['Q']]
        if n < 4:
            return []
        seen = [[False for _ in range(n)] for _ in range(n)]

        def isValid(path, n):
            # start = 0
            for i in range(0, n-1):
                for j in range(1, n):
                    # done checking j's
                    if i+j >= n:
                        break
                    if abs(path[i] - path[i+j]) == j:
                        #print(f" board failed: {path}, i,j = {i},{j}")
                        return False
                
                
                # if path[i] and path[]
                # if i == 4:
                #     if path[i-2]%2==0 and path[i]%2==0:
                #         return False 
            return True
                    
        def scan(row, col, path, left, n):
            if left < 0:
                return
            if len(path) == n and isValid(path, n):
                answer.append(path[:])
            for i in range(n):
                if not seen[row][i]:
                    seen[row][i] = True
                    path.append(i)
                    left -= 1
                    scan(row, i, path, left, n)
                    left += 1
                    path.pop()
                    seen[row][i] = False
          
        scan(0,0,[],n, n)
        base = '.'*n
        result = []

        print('Answer: ', answer)
        for i in range(len(answer)):
            temp = []
            for position in answer[i]:
                res = base[:position] + 'Q' + base[position+1:]
                temp.append(res)
            result.append(temp)
        return result