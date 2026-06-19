class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maximum = 0
        for i in range(n-1):
            maxPrice = max(prices[i+1:])
            if prices[i] < maxPrice:
                maximum = max(maxPrice-prices[i], maximum)

        return maximum


        
