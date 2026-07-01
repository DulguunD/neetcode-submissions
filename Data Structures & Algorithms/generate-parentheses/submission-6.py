class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]
        s = n*2
      
        def recurse(path, opening, closing):
            if len(path) == s-1:
                path += ')'
                result.append(path)
            if opening > 0:
                path += '('
                recurse(path, opening-1, closing)
                path = path[:-1]

            if closing >= opening:
                path += ')'
                recurse(path, opening, closing-1)
                path = path[:-1]

        recurse('(', n-1, n-1)
        return result
