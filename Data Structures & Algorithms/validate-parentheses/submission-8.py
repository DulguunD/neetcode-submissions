class Solution:
    def isValid(self, s: str) -> bool:
        pending = []
        length = len(s)
        opening = "({["
        closing = ")}]"
            
        for i in range(length):
            if s[i] in opening:
                pending.append(opening.index(s[i]))
            else:
                # if there was no opening
                if not pending:
                    return False
                print(f"Closing: {s[i]}, Found: {opening[closing.index(s[i])]}")
                if pending[-1] == closing.index(s[i]):
                    print(f"closed: {closing.index(s[i])}, pending: {pending}")
                    pending.pop()
                else:
                    return False
                    # pending.append(closing.index(s[i]))
              
        if len(pending) > 0:
            return False

        return True
        