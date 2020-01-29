'''
when split in half, there's always half of the array is sorted
either left
    if the target in the left part, then using bs to find it
or right
    same as left
'''

class Solution:
    def search(self, nums, target: int) -> int:
        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid = int((lo+hi)/2)
            if nums[mid] == target: return mid
            if nums[lo] <= nums[mid]: # left part is sorted
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else: # right part is sorted
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1


        return -1