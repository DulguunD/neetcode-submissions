class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        # if s.isspace():
        #     return 1
        counters = []
        seen = {}
        counter = 0
        left, right = 0, 0
        current = 0
        while current < length:
            if s[current] in seen:
                index = seen[s[current]]
                counters.append(counter)
                counter = 0
                seen = {}
                current = index+1
                left = current
                right = left
                continue
            seen[s[current]] = current
            counter += 1
            right += 1
            current += 1

        counters.append(counter)
        return max(counters)
    

        