class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        count=0
        
        if len(nums) ==0:
            return
        if 0 in nums:
            return 0
        for i in nums:
            if i<0:
                count += 1
        
        if count%2==0:
            return 1
        else:
            return -1