class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        
        aint=bint=0
        
        for i in range(len(a)):
            aint+=int(a[i])*(2**(len(a)-i-1))
    
            
        for i in range(len(b)):
            bint+=int(b[i])*(2**(len(b)-i-1))
    
        s=aint+bint
        
        output=""
        if s==0:
            output+="0"                 # 21%2 =1  21//2=4    4%2=0  4//2=2
        while s!=0:
            output+=str(s%2)
            s=s//2 
            
        return output[::-1]
            
        
        
