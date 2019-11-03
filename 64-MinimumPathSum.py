class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        D = {}
        def opt(g, i, j):
            if i == len(g)-1 and j == len(g[i])-1: return g[i][j]
            if i == len(g)-1:
                if D.get((i,j+1)) == None:
                    D[(i,j+1)] = opt(g, i, j+1)
                return D[(i,j+1)] +g[i][j]
            elif j == len(g[i])-1:
                if D.get((i+1,j)) == None: D[(i+1,j)] = opt(g, i+1, j)
                return D[(i+1,j)]+g[i][j]
            
            if D.get((i+1,j)) == None: D[(i+1,j)] = opt(g, i+1, j)
            if D.get((i,j+1)) == None: D[(i,j+1)] = opt(g, i, j+1)
            return min(D[(i+1,j)],D[(i,j+1)])+g[i][j]
                         
        
        if len(grid) == 0: return 0
        return opt(grid, 0 , 0)