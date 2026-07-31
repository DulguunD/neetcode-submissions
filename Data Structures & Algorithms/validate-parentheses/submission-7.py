class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        opening = "({["
        closing = ")}]"
            
        for i in range(length):
            if s[i] in opening:
                stack.append(opening.index(s[i]))
            else:
                if not stack:
                    return False
                print(f"Closing: {s[i]}, Found: {opening[closing.index(s[i])]}")
                if not stack:
                    return False
                if stack[-1] == closing.index(s[i]):
                    print(f"closed: {closing.index(s[i])}, stack: {stack}")
                    stack.pop()
                else:
                    stack.append(closing.index(s[i]))
              
        if len(stack) == 0:
            return True
        else:
            return False

        return True
        