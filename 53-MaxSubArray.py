class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0: return -2147483648

        ret = -2147483648
        res = 0
        for n in nums:
            res += n
            ret = max(ret,res)
            if n < 0 and res<= 0:
                res = 0
            ret = max(ret, n)

        return ret 
                
