class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        ans = [0 for i in range(2*nums_len)]
        for i,num in enumerate(nums):
            ans[i] = ans[i+nums_len] = num
        return ans