class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0

        for num in nums:
            if num-1 in numsSet:
                continue
            lenght = 1
            while num+lenght in numsSet:
                lenght += 1
            longest = max(lenght,longest)
        return longest