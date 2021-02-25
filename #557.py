class Solution:
    def reverseWords(self, s: str) -> str:
        
        result=""
        
        slist=s.split(" ")
        
        i=0
        while i<len(slist):
            result+=slist[i][::-1]+" "
            i+=1
        return result.strip()
