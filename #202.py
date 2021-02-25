class Solution:
    def next(self,n):
        total=0
        while n>0:
            total+=(n%10)**2
            n=n//10
        return total
    
    def isHappy(self, n: int) -> bool:
        check=[]
        
        while n not in check and n!=1:
            check.append(n)
            n=self.next(n)
            
        return n==1
            
