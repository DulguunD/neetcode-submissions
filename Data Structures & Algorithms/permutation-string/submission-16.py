class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        need = Counter(s1)
        window = Counter()
        for right in range(len(s2)):
            window[s2[right]] += 1
            if sum(window.values()) > len(s1):
                window[s2[left]] -= 1
                left += 1
            if window == need:
                return True
        return False
      