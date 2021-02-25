class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
          [1,2,2,5,2,3]
             ^|
          [2,5,6]
         
        """         
        if not nums2 : 
            return nums1                     
        p1, p2 = m-1, n-1
        cntr = len(nums1)-1
        
        while p1 >= 0 and p2 >= 0 :
            if nums1[p1] > nums2[p2] :
                nums1[cntr] = nums1[p1]
                cntr -= 1
                p1 -= 1
            else :
                nums1[cntr] = nums2[p2]
                cntr -= 1
                p2 -= 1
        
        if p2 >= 0 :
            
            nums1[:p2+1] = nums2[:p2+1]
            
            return nums1
        
