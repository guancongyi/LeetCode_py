class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        if r == 1 and c == 1:
            if obstacleGrid[0][0] == 1:return 0
            else: return 1
            
        dp = []
        for i in range(0, r):
            temp = []
            for j in range(0, c):
                temp.append(0)
            dp.append(temp)
        
        for i in range(0, c):
            if obstacleGrid[0][i] == 1: break
            else: dp[0][i] = 1
        
        for j in range(0, r):
            if obstacleGrid[j][0] == 1: break
            else: dp[j][0] = 1

        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):
                if obstacleGrid[i][j] == 1: dp[i][j] = 0
                else:
                    if i == 0 or j == 0: continue
                    else: dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]