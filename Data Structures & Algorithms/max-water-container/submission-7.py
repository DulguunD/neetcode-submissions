class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        length = len(heights)-1
        start, end = 0, len(heights)-1
        while start < end:
            area = max(area, (end-start)*min(heights[start], heights[end]))
            if heights[start] > heights[end]:
                end -=1
            else:
                start += 1
            # if end-start < height:
            #     end -= 1
            #     start = 0
            #     continue
            # if heights[start] < heights[end]:
            #     start += 1
            #     if start == end:
            #         start = 0
            # else:
            #     end -= 1
                # if start == end:
                #     end = length

            # width = end-start
            # area = max(area, width*height)
            # if height > width:
            #     end -= 1

            # start += 1
            # if start == end:
            #     end -= 1
            #     start = 0
            
        return area
        