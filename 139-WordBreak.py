class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        l = len(s)+1
        dp = [False]*l
        dp[0] = True
        for i in range(0,l-1):
            for j in range(0,i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        

        return dp[l-1]




s = Solution()
print(s.wordBreak("a",["a"]))