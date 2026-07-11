class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counters = []
        seen = {}
        length = len(s)
        if length == 0:
            return 0
        if length==1:
            return 1
        if s.isspace():
            return 1
        counter = 0
        left, right = 0, 0
        current = 0
        while current < length:
            # print(f"\tleft: {left}, right: {right}, counter: {counter}, current: {current}")
            # print(f"seen: {seen}")
            if s[current] in seen:
                index = seen[s[current]]
                # print(f"\tleft: {left}, right: {right}, counter: {counter}")
                # print(f"already seen index: {index}, value: {s[current]}")
                counters.append(counter)
                # counter = max(counter, right-left)
                counter = 0
                seen = {}
                current = index+1
                left = current
                # right = left+1
                right = left
                # counter += 1
                # continue
            seen[s[current]] = current
            counter += 1
            right += 1
            current += 1

        counters.append(counter)
        return max(counters)
    

        