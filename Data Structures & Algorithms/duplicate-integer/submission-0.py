class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = dict()
        for num in nums:
            map[num] = 1 + map.get(num, 0)
            if map[num] > 1:
                return True
        return False
