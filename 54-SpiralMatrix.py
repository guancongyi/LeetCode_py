class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])

        l, r, u, d = 0, n-1, 0, m-1
        
        res = []
        while l<=r and u<=d:
            # print(u,d,l,r)
            for i in range(l, r+1):
                res.append(matrix[u][i])
            u+=1
            
            
            for i in range(u, d+1):
                res.append(matrix[i][r])
            r-=1
            
            if u <= d:
                for i in range(r, l-1, -1):
                    res.append(matrix[d][i])
            d-=1
            
            if l <= r:
                for i in range(d, u-1, -1):
                    res.append(matrix[i][l])
            l+=1
            # print(res)
            
        return res
        