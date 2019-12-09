# def helper(x, y):
#     if x == 1 and y == 1:
#         return 1
#     elif y == 1:
#         return helper(x-1, y)
#     elif x == 1:
#         return helper(x, y-1)
#     else: 
#         return helper(x, y-1)+helper(x-1, y)
# return helper(m, n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1: return 1
        dp = []
        for i in range(0, n):
            temp = []
            for j in range(0, m):
                if i == 0 and j == 0: temp.append(0)
                elif j == 0: temp.append(1)
                elif i == 0: temp.append(1)
                else: temp.append(0)
            dp.append(temp)
    

        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):
                if i == 0 or j == 0: continue
                else: dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[n-1][m-1]

        
        

        

    
        