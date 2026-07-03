class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        length = len(candidates)
        def recurse(index, combinations, currentTarget):
            if currentTarget < 0:
                return
            if currentTarget == 0:
                result.append(combinations[:])
                return
            for i in range(index, length):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > currentTarget:
                    break
                combinations.append(candidates[i])
                recurse(i+1, combinations, currentTarget-candidates[i])
                combinations.pop()

        recurse(0, [], target)
        return result
      
        