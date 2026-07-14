from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        ans = 0
        max_freq = 0
        for right in range(len(s)):
            # print(f"\tleft: {left}, right: {right}, max_freq: {max_freq}, ans: {ans}")
            count[s[right]] += 1
            max_freq = max(max_freq, count[s[right]])

            # window_size = right-left+1
            # replacements_needed = window_size-max_freq

            # slide window to the left (shrink the window) - window is not valid
            while (right - left + 1) - max_freq > k:
                # print(f"left: {left}, left char: {s[left]} , count: {count}")
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans

      
      