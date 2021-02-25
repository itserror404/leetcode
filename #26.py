class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        l=len(nums)
        i=j=1                                         
        while i<l:                                                      
            if nums[i]!=nums[i-1]:                         
                nums[j]=nums[i]
                j=j+1
            i=i+1
        return j
                
                
        
            
        
