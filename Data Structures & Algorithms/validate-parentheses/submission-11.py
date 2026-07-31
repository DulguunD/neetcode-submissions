class Solution:
    def isValid(self, s: str) -> bool:
        pending = []
        length = len(s)
        opening = "({["
        closing = ")}]"
            
        for char in s:
            if char in opening:
                pending.append(char)
                continue

            # nothing to close 
            if not pending:
                return False

            if pending[-1] == opening[closing.index(char)]:
                pending.pop()
            else:
                # no matching opening
                return False
              
        if len(pending) > 0:
            return False

        return True
        