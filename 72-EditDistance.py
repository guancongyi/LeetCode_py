'''
dp midterm questions

note: the reason for making a 2d matrix with m+1 and n+1 is that 
        the first row and first column simply represent the empty word case

dp analysis:
1. if 2 letters are same, then simply check next one
2. otherwise, choose the min of insert, replace, and delete operation from last time

'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1), len(word2)        
        dp = [[0 for x in range(m+1)] for y in range(n+1)]
        
        for j in range(0, m+1):
            dp[0][j] = j

        for i in range(0, n+1):
            dp[i][0] = i

        print(dp)
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[j-1] == word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1) 

        print(dp)
        return dp[-1][-1]


# s = Solution()
# print(s.minDistance("abea","aaa"))
dp = [[x for x in range(2)] for y in range(5)]

print(dp)