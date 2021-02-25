class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if len(s)==0:
            return []
        
        count=output=0
        
        for i in s:
            if i!=" ":
                count+=1
                output=count
                
            else:
                count=0
                
        return output
                
