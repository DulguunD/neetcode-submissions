class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        start, end = 0, len(heights)-1
        # heights.sort()
        length = len(heights)-1
        current = 0
        # print(f'heights: {heights}')
        while start < end:
            height = min(heights[start], heights[end])
            width = end - start
            area = max(area, width*height)
            # print(f"start: {start}, end: {end}, area: {area}")
            # print(f" {heights[start]}, end: {heights[end]}, area: {area}")

            start += 1
            if start == end:
                end -= 1
                start = 0
            # if start == end:
            #     end = length
            # end -= 1
            # if start > 
            

            #
        return area
        