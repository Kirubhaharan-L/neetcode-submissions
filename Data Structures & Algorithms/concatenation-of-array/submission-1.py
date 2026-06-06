class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        for num in nums:
            nums.append(num)
            nums_len -= 1
            if nums_len == 0:
                break
        return nums