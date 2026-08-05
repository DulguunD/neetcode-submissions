class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 
        pending = []
        for index, height in enumerate(heights):
            newIndex = index
            while pending and pending[-1][0] > height:
                maxArea = max(pending[-1][0]* (index-pending[-1][1]), maxArea)
    
                discard = pending.pop()
                newIndex = discard[1]

            pending.append((height, newIndex))

        length = len(heights)
        while pending:
            popped = pending.pop()
            area = (length-popped[1])*popped[0]
            maxArea = max(maxArea, area)
      
        return maxArea
 

        
        