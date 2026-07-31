class Solution:
    def trap(self, height: List[int]) -> int:
            left = 0
            length = len(height)
            right = length-1
            result = 0
            leftMax = height[left]
            rightMax = height[right]

            while left < right and left < length:
                if leftMax < rightMax:
                    left += 1
                    leftMax = max(leftMax, height[left])
                    result += leftMax-height[left]
                else:
                    right -= 1
                    rightMax = max(rightMax, height[right])
                    result += rightMax-height[right]
            return result        
            
    