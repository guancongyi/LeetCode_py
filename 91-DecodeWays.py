'''
For each digit, check itself and the digit before it
if the first digit >= 1 and <= 9: then it adds dp[i-1]
if the seconde digit >= 10 and <=26: then it adds dp[i-2]
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        
        l = len(s)
        if l == 0: return 0
        dp = [0 for x in range(l+1)]
        dp[0] = 1
        if s[0] != '0': dp[1] = 1

        for i in range(2,l+1):
            first = int(s[i-1:i])
            second = int(s[i-2:i])
            # print(first, second)
            if first >= 1 and first <= 9:
                dp[i]+=dp[i-1]
            if second >= 10 and second <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]


s = Solution()
print(s.numDecodings("121"))