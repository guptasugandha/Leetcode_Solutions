class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi=0
        answer=[]
        for i in range(len(candies)):
            maxi=max(maxi, candies[i])
        
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxi:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer