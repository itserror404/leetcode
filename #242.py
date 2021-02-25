class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        canagram={}
        for i in s:
            if i not in canagram:
                canagram[i]=1
                
            else:
                canagram[i]+=1
                
        for i in t:
            if i not in canagram:
                canagram[i]=1000
            else:
                canagram[i]-=1

        
        for i in t:
            if canagram[i]!=0:
                return False
        return True
    
        # another method: create two dictss and compare
#another one that works: aadd 1 for each element in s, if it repeats add 1 again. Then subtract 1 for each element in t. If any has 0, then return false else true
