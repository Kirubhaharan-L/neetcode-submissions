from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        sorteds = hashmap.most_common(k)
        result = []
        for i in range(k):
            result.append(sorteds[i][0])
        return result