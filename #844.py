class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sstack=[]
        tstack=[]
        
        for i in S:
            if i!='#':
                sstack.append(i)
            elif i=='#' and sstack:
                sstack.pop()
        for i in T:
            if i!='#':
                tstack.append(i)
            elif i=='#' and tstack:
                tstack.pop()
                
        return "".join(sstack)=="".join(tstack)
                
                
