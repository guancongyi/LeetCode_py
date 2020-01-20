'''
same as #84
'''

class Solution:
    def maximalRectangle(self, matrix) -> int:
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        
        
        H = [ [0 for x in range(n)] for y in range(m)]
        for i in range(len(H)):
            for j in range(len(H[0])):
                if matrix[i][j] == "1":
                    if i > 0: H[i][j] = H[i-1][j]+1
                    else: H[i][j] = 1
                else: H[i][j] = 0
        
        print(H)
        res = 0
        for i in range(m):
            stk = [-1]
            Hrow = H[i]
            Hrow.append(0)
            for j in range(len(Hrow)):
                while Hrow[j] < Hrow[stk[-1]]:
                    tp = stk.pop()
                    h = Hrow[tp]
                    w = j - 1 - stk[-1]
                    res = max(res, w*h)
            
                stk.append(j)

        return res
        
s = Solution()
s.maximalRectangle([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
])