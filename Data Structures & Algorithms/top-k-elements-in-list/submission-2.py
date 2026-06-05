class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        count_list = [[v, k] for k,v in count.items()]
        count_list = sorted(count_list,reverse = True)
        result = []
        for i in range(k):
            count, num = count_list[i]
            result.append(num)
        return result