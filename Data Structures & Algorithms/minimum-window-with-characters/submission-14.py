class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length = len(s)
        positions = {}
        result = ""
        left, right = 0, 0
        solution = {}
        # ans = 0
        searching = {}

        for char in t:
            searching[char] = t.count(char)
        # print(f"searching: {searching}")

        def contains_t(substring: str) -> bool: 
            target = t[::]
            #print(f"contains t: substring:{substring}, t:{target}")
            for i in substring:
                if i in target:
                    for index, c in enumerate(target):
                        if c == i:
                            target = target[:index] + target[index+1:]
                            #print(f"popped '{i}', target:{target}")
                            break


            #print(f"done. target: {target}")
            return len(target) == 0

        if len(t) > len(s):
            return ""
        if s == t:
            return s
      
        

        # print(f"found: {found}")
        for right, char in enumerate(s):
            window = s[left:right+1]
            # print(f"current window: {window}")
            if char in t:
                # print(f"\tright found: {s[right]}")
                positions[char] = right
                # found.add(char)
                if contains_t(window):
                    # print(f"-   -   SOLUTION: {found}")
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
            # print(f"left: {left}, leftChar: {s[left]}, right: {right}, right char: {char}, window: {window}")
            # print(f"positions is updated: {positions}")
            # print(f"window: {window}, min: {result}")
       
            # print(f"left: {left}, leftChar: {s[left]}, right: {right}, right char: {s[right]}, window: {s[left:right]}")
        # print(f"-   -   -   final positions: {positions}")
        # print(f"\t*   *   * left: {left, s[left]}, right: {right, s[right]}, ans: {ans}")

        return result
       


       