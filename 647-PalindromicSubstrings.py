class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = []
        l = len(s)
        for i in range(0, l):
            dp.append([])
            for j in range(0, l):
                dp[i].append(0)
        
        count = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s), 1):
                
                if (s[i] == s[j]) and ( (j-i < 3) or (dp[i+1][j-1]==1)):
                    dp[i][j] = 1


        count = sum(x.count(1) for x in dp)
        return count

