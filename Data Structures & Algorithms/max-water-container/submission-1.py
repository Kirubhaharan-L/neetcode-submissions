class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        for l in range(len(heights)):
            for r in range(len(heights)-1,-1,-1):
                if l == r:
                    break
                # area = width * length
                width = r - l
                lenght = min(heights[l], heights[r])
                area = width * lenght
                maximum = max(area, maximum)
        return maximum