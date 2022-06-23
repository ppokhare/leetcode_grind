class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #idea1: two loops:check every posibilites to buy and sell.
        # result = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         gain =  prices[j] - prices[i]
        #         result = max(result, gain)
        # return result
    
        #idea2: buy when price is good; buy low sell high
        if len(prices) == 0: return 0
        buy = prices[0]
        result = 0
        for p in prices:
            if p < buy: buy = p
            gain = p-buy
            result = max(gain,result)
        return result