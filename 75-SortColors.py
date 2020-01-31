class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        begin, i, end = 0, 0, len(nums)-1
        
        while i <= end:
            if nums[i] == 0:
                nums[begin], nums[i] = nums[i], nums[begin]
                i+=1
                begin+=1
            elif nums[i] == 2:
                nums[end], nums[i] = nums[i], nums[end]
                end-=1
            else:
                i+=1
                
        print(nums)