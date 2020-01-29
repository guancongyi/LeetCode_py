class Solution:
    def findMin(self, nums) -> int:
        lo = 0
        hi = len(nums)-1

        res = float('inf')
        while lo <= hi:
            mid = int((lo+hi)/2)
            if nums[lo] <= nums[mid]: # left part is sorted
                res = min(res, nums[lo])
                lo = mid+1
                
            else: # right part is sorted
                res = min(res, nums[mid])
                hi = mid-1


        return res