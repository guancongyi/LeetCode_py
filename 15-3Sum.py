class Solution:
    def threeSum(self, nums):
        nums.sort()
        # put target value in the newArray
        newArray = []
        for i in range(0, len(nums)):
            newArray.append(0-nums[i])

        # for each num in newArray, do two sum
        result = []
        rep = {}
        for i in range(0, len(newArray)):
            if i>0 and newArray[i-1] == newArray[i]: continue
            target = newArray[i]
            d = {}
            
            for j in range(i+1, len(nums)):                    
                if d.get(nums[j]) != None:
                    if rep.get((0-target, target-nums[j], nums[j])) != None:continue
                    else:
                        rep[(0-target, target-nums[j], nums[j])] = 1
                        result.append([0-target, target-nums[j], nums[j]])
                else: d[target-nums[j]] = 1

        return result   



        

