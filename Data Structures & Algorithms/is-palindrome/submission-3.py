import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

        # clean = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        # n =  len(clean)
        # j = n - 1
        # for i in range(n):
        #     if clean[i] != clean[j]:
        #         return False
        #     j -= 1
        # return True

        