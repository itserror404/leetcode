class Solution:
    def minimumOperations(self, nums: List[int]) -> int:  
        counter=0
        while nums:
            nums= [i for i in nums if i>0]
            
            if nums:
                mini= min(nums)
                nums= [ i-mini for i in nums]
                counter+=1
            else:
                return counter
           