class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        leng=len(x)
        if leng==1:
            return True
        else:
            for i in range(0, leng//2):
                if x[i]!=x[leng-i-1]:
                    return False
            return True
        
