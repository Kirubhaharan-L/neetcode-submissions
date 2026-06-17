class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maximum = 0
        for l in range(n):
            for r in range(l+1,n):
                lenght = r - l
                width = min(heights[l],heights[r])
                area = lenght * width
                maximum = max(area, maximum)
        return maximum

            
