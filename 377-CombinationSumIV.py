'''
Same thought as coin change problem, but this 
problem allows different combinations

for every number i from 0 to target,
if i >= num from id 0 to id len(nums)-1
dp[i] = dp[i-num]
'''


class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0 for x in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            for j in range(0, len(nums)):
                if nums[j] <= i:
                    dp[i] += dp[i-nums[j]]

        return dp[-1]


s = Solution()
print(s.combinationSum4([1,2,3],4))