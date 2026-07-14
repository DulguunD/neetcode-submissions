class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        char = s[0]
        left, right, longest = 0, 0, 0
        reps = k
        nextIndex = 0
        while right < length:
            # print(f"\tleft: {left}, right: {right}, reps: {reps}, long: {longest}")
            if s[right] == char:
                longest = max(longest, right-left+1)
            else:
                if nextIndex == -1:
                    nextIndex = right
                if reps > 0:
                    reps -= 1
                    # print(f"left: {left}, right: {right}, reps: {reps}, long: {longest}")
                    longest = max(longest, right-left+1)
                else:
                    # find next window
                    # print(f"current: {s[right]}, shifting left from {left}, right: {right}")
                    left = nextIndex
                    right = nextIndex
                    nextIndex = -1
                    # print(f"    shifted left to {left}, right: {right}")
                    char = s[right]
                    reps = k
                    continue
            right += 1

            if right == length:
                if reps > 0:
                    leftSize = min(left,reps)
                    size = right-left+leftSize
                    longest = max(longest, size)
            
                if nextIndex != -1:
                    left = nextIndex
                    right = nextIndex
                    nextIndex = -1
                    # print(f"    shifted left to {left}, right: {right}")
                    char = s[right]
                    reps = k

        return longest


      