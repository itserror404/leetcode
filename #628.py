class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()           #[-6,-5,1,2,3,4,]
        
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[1]*nums[0] )
        
