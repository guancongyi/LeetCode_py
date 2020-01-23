class Solution:
    def maximalSquare(self, matrix) -> int:
        m = len(matrix)
        if m==0: return 0
        n = len(matrix[0])
        if n==0: return 0
        dp = [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
        

        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1


        print(dp)
        return (max(map(max,dp)))**2
        


s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))