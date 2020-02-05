class Solution:
    def helper(self, nums, target, k, curr):
        res = []
        if k == 2:
            l,r = curr,len(nums)-1
            while l < r:
                if nums[l]+nums[r] == target:
                    ret = [nums[l],nums[r]]
                    res.append(ret)
                    while l<r and nums[l] == nums[l+1]:l+=1
                    while l<r and nums[r] == nums[r-1]:r-=1
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    r-=1
                        
        else:
            for i in range(curr, len(nums)-(k-1)):
                if i>curr and nums[i] == nums[i-1]: 
                    continue
                temp = self.helper(nums,target-nums[i], k-1, i+1)
                for j in temp:
                    res.append([nums[i]]+j)
                
                
        return res
        
        
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        return self.helper(nums, target, 4, 0)
            
            