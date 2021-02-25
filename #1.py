class Solution:
    def twoSum(self, listt: List[int], target: int) -> List[int]:
        compliment={}
        for index, i in enumerate(listt):
            if compliment.get(i) is None:
                compliment[target-i]=index 
            else:
                return [compliment[i], index]
        
