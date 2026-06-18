class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maximum = 0
        l , r = 0 , n-1

        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            maximum = max(area, maximum)
            if l < r and heights[l] >= heights[r]:
                r -= 1
            elif l < r:
                l += 1
        return maximum
