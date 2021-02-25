class Solution:
     def countPrimes(self, n: int) -> int:
            def prime(n):
                from math import sqrt
                if n<=1:
                    return True
                
                for i in range(2,int(sqrt(n))+1):
                    if n%i==0:
                        return False
                return True
            
            count=0
            for num in range(2,n):
                if prime(num)==True:
                    count+=1
                
            return count
     
 
