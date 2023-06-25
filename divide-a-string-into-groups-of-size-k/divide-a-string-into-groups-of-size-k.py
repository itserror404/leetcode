class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans=[]
        
        for i in range(0, len(s), k):

            if len(s[i: i+k]) == k:
                ans.append(s[i:i+k])
            if len(s[i: i+k])<k:
                a=s[i: i+k]+ fill*( k-len (s[i: i+k]) )
                ans.append(a)
            
        return ans
            
    
        
            