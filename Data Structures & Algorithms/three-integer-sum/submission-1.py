class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        # a + b + c = 0
        for i, a in enumerate(nums):
            # if array contains only positive can never be sum == 0
            if a > 0:
                break
            # this is to skip duplicate numbers
            if i > 0 and a == nums[i - 1]:
                continue
            l , r = i + 1, n -1
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if  three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l , r = l + 1, r - 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res