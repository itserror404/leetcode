class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
             
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
   
        
        
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
            
        return (len(nums))
        
