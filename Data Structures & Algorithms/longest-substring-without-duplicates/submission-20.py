class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left, longest = 0, 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]]+1
            seen[s[right]] = right
            longest = max(longest, right-left+1)

        return longest