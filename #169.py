class Solution:
    def majorityElement(self, num: List[int]) -> int:
        
        count={}
        if len(num)==1:
            return num[0]
        for i in num:
            if i not in count:
                count[i]=1
            elif i in count:
                count[i]+=1
                
            if count[i]>len(num)/2:
                return i
        print(count)
            
        
