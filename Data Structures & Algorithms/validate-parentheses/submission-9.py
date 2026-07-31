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

            # if there was no opening
            if not pending:
                return False

            if pending[-1] == opening[closing.index(char)]:
                pending.pop()
            else:
                # nothing to close
                return False
              
        if len(pending) > 0:
            return False

        return True
        