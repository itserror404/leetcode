class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l=len(digits)-1                      # [1,2,3]---> [1,2,4]
                                             # [1,2,9]---> [1,3,0]
                                             # [9,9,9]---> [1,0,0,0]
        while l>=0: 
            if digits[l]==9:
                digits[l]=0
            else:
                digits[l]+=1
                return digits
            l-=1     
        return [1]+digits 
        
            
            
