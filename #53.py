class Solution:
    def maxSubArray(self, n: List[int]) -> int:
        
        #  [-2,1,-3,4,-1,2,1,-5,4]
        #    T= max(T+i, i)= max(-1,1)=1===> max(1+-3, -3)=max(-2, 3)=3=max(-3+4,4)==3
        #   1,-2,4,3,5...
        #    M=1,1,4,4,5,5,5
        
        tsum=msum=n[0]
        for i in n[1:]:
            if tsum+i>i:
                tsum=tsum+i
            else: 
                tsum=i
                
            if tsum>msum:
                msum=tsum
                
        return msum
