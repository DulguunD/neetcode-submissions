class Solution:
    def minWindow(self, s: str, t: str) -> str:
        result = ""
        left, right = 0, 0
        if len(t) > len(s):
            return ""
        if s == t:
            return s

        def contains_t(substring: str) -> bool: 
            target = t[::]
            for char in substring:
                if char in target:
                    for index, c in enumerate(target):
                        if c == char:
                            target = target[:index] + target[index+1:]
                            break
            #print(f"done. target: {target}")
            return len(target) == 0

        for right, char in enumerate(s):
            window = s[left:right+1]
            # print(f"left: {left}, leftChar: {s[left]}, right: {right}, right char: {char}, window: {window}")
            if char in t:
                if contains_t(window):
                    # is left char not needed in substring
                    while s[left] not in t or contains_t(s[left+1:right+1]):
                        left += 1

                    window = s[left:right+1]
                    # print(f"found new substring: {window}")
                    if len(result) == 0:
                        result = window 
                    if len(window) < len(result):
                        result = window
            window = s[left:right+1]
        return result
       


       