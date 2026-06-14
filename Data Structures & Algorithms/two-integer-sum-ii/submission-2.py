class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        for i in range(n):
            tmp = target - numbers[i]
            l, r = i + 1, n - 1
            while l <= r:
                mid = l + (r-l) // 2
                if numbers[mid] == tmp:
                    return [i+1, mid+1]
                elif numbers[mid] > tmp:
                    r = mid - 1
                else:
                    l = mid + 1
            