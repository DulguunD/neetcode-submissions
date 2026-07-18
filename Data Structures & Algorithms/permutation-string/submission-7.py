class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        found = defaultdict(int)
        need = Counter(s1)
        required = len(s1)
        for right, char in enumerate(s2):
            found[char] += 1
            while left < right and (s2[left] not in s1 or found[s2[left]] > need[s2[left]]):
                found[s2[left]] -= 1
                left += 1

            if right-left+1==required:
                same = True
                for key in need.keys():
                    if need[key] != found[key]:
                        same = False
                        break
                      
                if same:
                    return True
            # print(f"left: {left}, right: {right}, window: {window}, found: {found}")
        return False


        