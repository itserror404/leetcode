class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)==0:
            return 0
        
        buy=prices[0]
        profit=0
        
        for i in (prices):
            if i<buy:
                buy=i
            else:
                profit=max(profit, i-buy)
        return profit
        
