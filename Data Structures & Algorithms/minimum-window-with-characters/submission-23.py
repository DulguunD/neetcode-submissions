from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        result = ""
        length = len(s)
        window = defaultdict(int)
        need = Counter(t)
        formed = 0

        left = 0
        required = len(need)
        best_left, best_right = 0,0
        best_len = float("inf")

        for right, char in enumerate(s):
            window[char] += 1

            if window[char] == need[char]:
                formed += 1

            while formed == required:
                window_len = right-left+1
                if window_len < best_len:
                    best_len = window_len
                    best_left = left
                    best_right = right 
                    
                left_char = s[left]
                window[left_char] -= 1
                if window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
                
        if best_len == float("inf"):
            return ""

        return s[best_left:best_right+1]
       


       