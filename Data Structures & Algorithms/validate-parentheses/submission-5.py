class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        opening = "({["
        closing = ")}]"
            
        for i in range(length):
            print(f"char: {s[i]}, stack: {stack}")
            if s[i] in opening:
                stack.append(opening.index(s[i]))
            elif s[i] in closing :
                print(f"Closing: {s[i]}, Found: {opening[closing.index(s[i])]}")
                if not stack:
                    return False
                if stack[-1] == closing.index(s[i]):
                    print(f"closed: {closing.index(s[i])}, stack: {stack}")
                    stack.pop()
                else:
                    stack.append(closing.index(s[i]))
          

        print(f"Final Stack: {stack}")

        if len(stack) == 0:
            return True
        else:
            return False
        return True
        