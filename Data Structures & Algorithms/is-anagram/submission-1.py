from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = dict()
        d2 = dict()
        for i in range(len(s)):
            if s[i] in d1:
                d1[s[i]] += 1
            else:
                d1[s[i]] = 1
            if t[i] in d2:
                d2[t[i]] += 1
            else:
                d2[t[i]] = 1
        # print('D1: ', d1)
        # print('D2: ', d2)
        return d1 == d2
        return True

        