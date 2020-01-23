'''
opt(i) = the minimum number of coins used for amount i
opt(i) has following cases:
1. i == one of the coin types
2. i != '' '' '' '' Therefore we should find out the min change
among all coin types.
'''

class Solution:
    def coinChange(self, coins, amount: int) -> int:
        n = len(coins)
        if n == 0 and amount == 0: return 0
        if n == 0: return -1
        if amount == 0: return 0
        dp = [float('inf') for x in range(amount+1)]
        dp[0] = 0
            
        for i in range(1, amount+1):
            for j in range(0, n):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)

        
        # print(dp)
        if dp[-1]==float('inf'): return -1
        return dp[-1]  
s = Solution()
print(s.coinChange([1,2,5], 5))