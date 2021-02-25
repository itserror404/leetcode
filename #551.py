class Solution:
    def checkRecord(self, s: str) -> bool:
        
        a=s.count("A")
        
        if a>1:
            a=False
        else:
            a=True
        
        i=0
        while i<len(s) and i+1<len(s) and i+2<len(s):
            if s[i]==s[i+1]==s[i+2]=="L":
                a=False
            i+=1
                
        return a
