'''
2 states: can buy and can sell
dp based on them


dp[][] == current best profit for buying or selling

1. if I don't have any stock, which means i can either buy or wait
dp[i][0] = max(dp[i-1][1]+p[i], dp[i-1][0] )

2. if I have stock, which means I can either sell or keep, and wait for 2 days if I sell
dp[i][1] = max(dp[i-2][0]-p[i], dp[i-1][1] )


'''



# def OPT(i, a, prices):
#     if i > len(prices)-1:
#         return 0
#     if a: # bought
#         # keep or sell
#         return max(OPT(i+1, 1, prices), OPT(i+2, 0, prices) + prices[i] )
#     else:
#         # buy or skip
#         return max(OPT(i+1, 1, prices) - prices[i], OPT(i+1, 0, prices) )


# class Solution:
#     def maxProfit(self, prices) -> int:
#         return OPT(0, 0, prices)
        

class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0: return 0
        dp = [[0 for x in range(2)] for y in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][1]+prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1])
        print(dp)

        return max(dp[len(dp)-1][0], dp[len(dp)-1][1])
        

s = Solution()
s.maxProfit([1,2,3,4,55,6]) 