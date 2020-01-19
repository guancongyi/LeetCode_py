'''
dp :

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [ [0 for y in range(len(s)+1)] for x in range(len(p)+1)]
        
        dp[0][0] = 1
        
        for i in range(1, len(p)+1):
            if p[i-1] == '*': dp[i][0] = 1
            else: break

        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if (s[j-1] == p[i-1] or p[i-1] == '?') and dp[i-1][j-1] == 1:
                    dp[i][j] = 1
                elif p[i-1] == '*' and (dp[i-1][j] or dp[i][j-1]):
                    dp[i][j] = 1

        # print(dp)
        return dp[len(p)][len(s)]    
            


s = Solution()
s.isMatch("adceb", "*dceb")