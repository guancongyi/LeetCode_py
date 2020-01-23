'''
outer loop is coin type to avoid repeated pattern
The idea is simple: 
for each amount, calculate the total number of ways to form them
using every coin type:
WAYS(i) = WAYS(i-c1)+WAYS(i-c2)+... for all c <= i
'''

class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0 for x in range(amount+1)]

        # for i in range(amount+1):
        #     if i % coins[0] == 0: dp[i] = int(i/coins[0])
                
        dp[0] = 1
        for j in range(0, len(coins)):
            for i in range(1, amount+1):
                if i >= coins[j]:
                    dp[i] += dp[i-coins[j]]
            
                    
        # print(dp)

        return dp[-1]