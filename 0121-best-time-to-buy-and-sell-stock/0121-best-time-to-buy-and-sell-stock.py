class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #n^2 time: two loop buy at i and check if selling at j is profitable
        # n time: buy low sell high: when you find the cheaper price no need to complete the loop
        result = 0
        b = 0
        
        for i in range(1,len(prices)):
            if prices[i] <prices[b]: b=i
            else: 
                profit = prices[i] - prices[b]
                result = max(result, profit)
        return result
        