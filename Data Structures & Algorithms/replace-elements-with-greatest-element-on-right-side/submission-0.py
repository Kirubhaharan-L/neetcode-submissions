class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = [0 for i in range(len(arr))]
        for i,num in enumerate(arr):
            if i != len(arr)-1:
                max_num = max(arr[i+1:])
                result[i] = max_num
            else:
                result[i] = -1
        return result

