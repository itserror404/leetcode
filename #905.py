class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result=[]
        for i in A:
            if i%2==0:
                result.append(i)
                
        for i in A:
            if i%2!=0:
                result.append(i)
                
        return result
    
    
