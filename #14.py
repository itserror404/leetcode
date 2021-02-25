class Solution:
    def longestCommonPrefix(self, n: List[str]) -> str:
        
        if len(n)==0:
            return ""
        
        if len(n)==1:
            return n[0]
        
        prefix=n[0]
        pleng=len(prefix)
        
        for i in n[1:]:
            
            while prefix !=i[0:pleng]:
                prefix=prefix[0:pleng-1]
                pleng-=1
                
        return prefix

    
        
                
            
                    
                    
