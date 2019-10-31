class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = []
        l = len(s)
        for i in range(0, l):
            dp.append([])
            for j in range(0, l):
                dp[i].append(0)

        mx = 0
        mxPair = (0,0)

        for i in range(l-1, -1, -1):
            for j in range(i, l, 1):
                if (s[i] == s[j] )and ( (j-i < 3) or dp[i+1][j-1]==1):
                    dp[i][j] = 1

                if dp[i][j] and (j-i+1 > mx): 
                    mxPair = (i, j)
                    mx = j-i+1


        return s[mxPair[0]: mxPair[1]+1]
