'''
easy
can improve
'''

class Solution:
    def lengthOfLIS(self, nums) -> int:
        m = len(nums)
        if m == 0: return 0
        dp = [1 for x in range(m)]
        res = 0
        for i in range(0, m):
            cur = nums[i]
            for j in range(0, i):
                if nums[j]<cur:
                    dp[i] = max(dp[i], dp[j]+1)
            res = max(dp[i], res)

        return res

s = Solution()
print(s.lengthOfLIS([10,7,9,2,5,3,7,101,18]))