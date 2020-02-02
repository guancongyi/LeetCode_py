class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = float('inf')
        tempMin = float('inf')
        
        for i in range(0, len(nums)-1):
            l,r = i+1,len(nums)-1
            
            while l < r:
                s = nums[l] + nums[i] +nums[r]
                if s > target:
                    r-=1
                    tempMin = min(tempMin, abs(s-target))
                    if tempMin == abs(s-target): res = s
                elif s < target:
                    l+=1
                    tempMin = min(tempMin, abs(s-target))
                    if tempMin == abs(s-target): res = s
                else:
                    return s
        
        return res