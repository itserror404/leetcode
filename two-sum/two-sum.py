class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result={}
       
        
        for i in range(0, len(nums)):
            if result.get(nums[i])==None:
                result[target-nums[i] ]= i
            else:
                return [i, result[nums[i]]]
            
            

            
            
            
        