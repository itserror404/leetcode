class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        compliment={}
        for index,num in enumerate(numbers):
            if compliment.get(num) is None:
                compliment[target-num]=index     
            else:
                output=[compliment[num]+1,index+1]
                return output   
