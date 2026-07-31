class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)
        half = length // 2
        # if length % 2 != 0:
        #     return False

        braces = "(){}[]"
        opening = "({["
        closing = ")}]"
            
        for i in range(length):
            # stack.append(s[i])
            # stack.append
            print(f"char: {s[i]}, stack: {stack}")
            if s[i] in opening:
                # stack.append(s[i])
                idx = opening.index(s[i])
                stack.append(idx)
                # print(f"character: {s[i]}, index: {idx}")
            elif s[i] in closing :
                print(f"Closing: {s[i]}, Found: {opening[closing.index(s[i])]}")
                if not stack:
                    return False
                if stack[-1] == closing.index(s[i]):
                    print(f"closed: {closing.index(s[i])}, stack: {stack}")
                    stack.pop()
                else:
                    stack.append(closing.index(s[i]))
                # stack.pop()
                # if not stack:
                #     return False
                # if stack:
                #     stack.pop()
             

        print(f"Final Stack: {stack}")

        if len(stack) == 0:
            return True
        else:
            return False
        # print(f"stack: {stack}")

        # for i in range(half, length):
        #     char = stack.pop()
        #     print(f"comparing: {char},  {s[i]}")
        #     if char != s[i]:
        #         return False
        

        return True
        