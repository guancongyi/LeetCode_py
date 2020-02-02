'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        res = []
        for i in range(0, len(nums)):
            
            if nums[i] not in dict:
                
                dict[target-nums[i]] = 1
            elif dict[nums[i]]:
                # print(i,dict)
                res.append(i)
                res.append(nums.index(target-nums[i]))
                break
        
        return res