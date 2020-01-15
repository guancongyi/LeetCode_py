class Solution:
    def numTrees(self, n) -> int:
        G = {0:1, 1:1, 2:2}
        F = [[0 for x in range(n+1)] for y in range(n+1)]
        for i in range(1, n+1):
            for j in range(i,n+1):
                F[i][j] = G[i-1]*G[j-i]

        res = sum(row[n] for row in F)

        return res
        


s = Solution()
s.numTrees(3)