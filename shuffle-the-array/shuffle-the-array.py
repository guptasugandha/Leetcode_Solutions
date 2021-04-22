class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer=[]
        n=int(len(nums)/2)
        for i in range(int(len(nums)/2)):
            answer.append(nums[i])
            answer.append(nums[i+n])
        
        return answer