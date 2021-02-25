class Solution:
    def toLowerCase(self, str: str) -> str:
        
        strlist=list(str)
     
        i=0
        while i <(len(strlist)):
            if strlist[i].isupper()==True:
                strlist[i]=strlist[i].lower()
            i+=1
                
        return "".join(strlist)
                
                
                
