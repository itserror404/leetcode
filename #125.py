class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        string=""
        
        for i in range(0, len(s)):
            if s[i].isalnum()==True:
                string+=(s[i]).lower()
            
            
        for i in range(0, len(string)//2):
            if string[i]!=string[-i-1]:
                return False
        return True
    
    
