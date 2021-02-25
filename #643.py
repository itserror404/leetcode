class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum=sum(nums[0:k])
        pointer=maxsum
        
        for i in range(k, len(nums)):
            pointer+=nums[i]
            pointer-=nums[i-k]
            
            maxsum=max(maxsum, pointer)
            
        return maxsum/k
