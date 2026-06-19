class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        
        preMax = [0] * n
        postMax = [0] * n
        maximum = 0

        for i,num in enumerate(height):
            if i == 0:
                preMax[i] = 0
                postMax[i] = max(height[i+1:])    
            elif i == n-1:
                preMax[i] = max(height[:i])
                postMax[i] = 0
            else:
                preMax[i] = max(height[:i])
                postMax[i] = max(height[i+1:])

        for i,num in enumerate(height):
            store = min(preMax[i],postMax[i]) - num
            if store > 0:
                maximum += store

        return maximum