class Solution:
    def mctFromLeafValues(self, arr) -> int:
        res = 0
        for i in range(0, len(arr)-1):
            mn = arr.index(min(arr))
            if 0<mn<len(arr)-1:
                res += min(arr[mn-1],arr[mn+1])*arr[mn]
            else:
                if mn == 0: res+= arr[mn]*arr[1]
                else: res += arr[mn]*arr[mn-1]
                    
            arr.pop(mn)
                    
        return res