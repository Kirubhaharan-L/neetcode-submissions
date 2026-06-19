class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        maxBuy = 0
        if n < 2:
            return 0
        while r < n:
            if prices[l] > prices[r]:
                l, r = r, r + 1
            elif prices[l] < prices[r]:
                buy = prices[r] - prices[l]
                maxBuy = max(buy, maxBuy)
                r += 1
            else:
                r +=1
              
        return maxBuy