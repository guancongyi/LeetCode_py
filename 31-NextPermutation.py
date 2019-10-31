class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        i = len(nums)-2
        if(i < 0): return None
        while nums[i] >= nums[i+1]:
            i-=1
            if i < 0: 
                nums.reverse()
                flag = 1
                break
            
        if not flag:
            mn = float('inf')
            id = -1
            for k in range(i, len(nums)):
                if nums[k] > nums[i] and nums[k] <= mn:
                    print(nums[k])
                    mn = nums[k]
                    id = k

            nums[i], nums[id] = nums[id], nums[i]

            temp = nums[i+1:][::-1]
            nums[i+1:] = temp