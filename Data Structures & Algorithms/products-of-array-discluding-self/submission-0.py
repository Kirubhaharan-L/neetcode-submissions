import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        left = list(output)
        right = list(output)
        i = 0
        while i < len(nums):
            j = i
            if j == 0:
                left[i] = 1
            else:
                while j > 0:
                    j -= 1
                    left[i] *= nums[j]
            i += 1

        i = len(nums) - 1
        while i >= 0:
            j = i
            if j == len(nums)-1:
                right[i] = 1
            else:
                while j < len(nums)-1:
                    j += 1
                    right[i] *= nums[j]
            i -= 1
        for i, num in enumerate(nums):
            output[i] = left[i] * right[i]
        return output