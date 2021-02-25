class Solution:
    def isValid(self, s: str) -> bool:
        
        dup = []
        match = {')':'(', ']':'[', '}':'{'}
        
        
        if len(s)%2!=0:
            return False
        
        for i in range(0,len(s)):
            
            if s[i] in "([{":
                dup.append(s[i])
                
            else:
                if dup and dup[-1]==match[s[i]]:
                    dup.pop()
                else:
                    return False
                
        return len(dup)==0
        
        
       
