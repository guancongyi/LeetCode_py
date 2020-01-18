class Solution:
    def numTrees(self, n) -> int:
        G = dict.fromkeys(range(n+1),0)
        G[0] = G[1] = 1
        for i in range(2, n+1):
            for j in range(1,i+1):
                G[i] += G[j-1]*G[i-j]


        return G[n]
        


s = Solution()
s.numTrees(4)