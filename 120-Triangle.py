class Solution:
    def minimumTotal(self, triangle) -> int:
        D = {}
        def findMin(T, i, j):
            if i == len(T)-1: return T[i][j]
            else:
                if D.get((i+1,j)) == None:D[(i+1,j)] = findMin(T, i+1, j)
                if D.get((i+1,j+1)) == None: D[(i+1,j+1)] = findMin(T, i+1, j+1)
                
                return min(D.get((i+1,j)), D.get((i+1,j+1)))+T[i][j]
        
        return findMin(triangle, 0, 0)

    