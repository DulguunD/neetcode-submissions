import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        n =  len(clean)
        j = n - 1
        for i in range(n):
            if clean[i] != clean[j]:
                return False
            j -= 1
        return True

        