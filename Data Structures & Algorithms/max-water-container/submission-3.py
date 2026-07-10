class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        start, end = 0, len(heights)-1
        while start < end:
            height = min(heights[start], heights[end])
            area = max(area, (end-start)*height)
            start += 1
            if start == end:
                end -= 1
                start = 0
        return area
        