class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i=0 
        count=0                                  # [2,2,2,2,2,2,2,2]  , 2
                                                                  ^
                                                      ^
                                                  #[0,1,3,0,4]

        while i<len(nums):
            if nums[i]!=val:
                nums[count]=nums[i]
                count+=1                      
            i=i+1 
            
                
        return count
    
    
    
        while nums.count(val):
            nums.remove(val)
            
        return len(nums)
                
        
