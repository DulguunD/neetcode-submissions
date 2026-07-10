class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        start, end = 0, len(heights)-1
        while start < end:
            area = max(area, (end-start)*min(heights[start], heights[end]))
            if heights[start] > heights[end]:
                end -=1
            else:
                start += 1
        return area
        