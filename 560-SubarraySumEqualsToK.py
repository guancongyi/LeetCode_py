class Solution:
    def subarraySum(self, nums, k: int) -> int:
        freq, count, subSum = {0:1}, 0, 0
        for i in range(0, len(nums)):
            subSum += nums[i]
            if freq.get(subSum-k) != None:
                count+=freq.get(subSum-k)
            if freq.get(subSum) == None: freq[subSum] = 1
            else: freq[subSum] += 1

        return count
s = Solution()
# s.subarraySum([4,2,2,3,2,4,1], 5)
# s.subarraySum([-1,-1,3,-1], 2)
# s.subarraySum([-1,1,1], 2)
s.subarraySum([5], 5)
# s.subarraySum([5,5], 5)
# s.subarraySum([-1,-2,3,0], 0)
# s.subarraySum([0,0,0,0], 0)




