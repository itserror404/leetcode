class Solution:
    def reverse(self, n: int) -> int:
        
        neg=False
        if n*-1==abs(n):
            neg=True
        n=abs(n)
        
        reverse=0
        
        for i in range(len(str(n))):
            reverse=reverse*10+(n%10)
            n=n//10
            
        if neg==True:
            reverse=reverse*-1
	    
        return reverse

        
        
