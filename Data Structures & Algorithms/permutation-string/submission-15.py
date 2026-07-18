class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        length = len(s2)
        need = Counter(s1)
        window = Counter()
        for right in range(length):
            # print(f"window: {window}")
            window[s2[right]] += 1
            if sum(window.values()) > len(s1):
                window[s2[left]] -= 1
                left += 1
            
            if window == need:
                return True
        return False
        # while right < length:
        #     if 
        # left = 0
        # found = defaultdict(int)
        # need = Counter(s1)
        # required = len(s1)
        # matches = 0
        # for right, char in enumerate(s2):
        #     found[char] += 1
        #     # print(f"left: {left}, right: {right}")
        #     if found[char] == need[char]:
        #         matches += 1
        #         print(f"matched char: {char}, updated matches: {matches}")
        #     while left <= right and (s2[left] not in s1 or found[s2[left]] > need[s2[left]]):
        #         left_char = s2[left]
        #         if found[left_char] == need[left_char]:
        #             matches -= 1
        #         # matches -= 1
        #         found[left_char] -= 1
        #         left += 1

        #     if matches == required and right-left+1==required:
        #         return True
    
        # return False


        