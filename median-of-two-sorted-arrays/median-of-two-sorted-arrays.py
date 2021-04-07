class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1+nums2)
        
        print(nums3)
        
        l=len(nums3)
        print(l)
        
        median=0
        
        if l%2==0:
            mid=int((l/2)-1)
            nextmid=int(l/2)
            median = (nums3[nextmid] + nums3[mid])/2
        else:
            mid=ceil(l/2) -1
            print(mid)
            median = nums3[mid]
            
        print(median)
        return median