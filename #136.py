class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        count={}
        
        for i in nums:
            if count.get(i) is None:
                count[i]=nums.count(i)
                
        for i in count:
            if count.get(i)==1:
                return i
            
            
            
            
