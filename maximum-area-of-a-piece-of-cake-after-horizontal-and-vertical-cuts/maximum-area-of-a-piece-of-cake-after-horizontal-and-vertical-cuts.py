class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        maxHeight = max(horizontalCuts[0], h-horizontalCuts[-1])
        maxWidth = max(verticalCuts[0], w-verticalCuts[-1])
        
        for i in range(1, len(horizontalCuts)):
            maxHeight = max(maxHeight, horizontalCuts[i]-horizontalCuts[i-1])
            
        for i in range(1, len(verticalCuts)):
            maxWidth = max(maxWidth, verticalCuts[i]-verticalCuts[i-1])
            
        return (maxHeight*maxWidth)%(10**9 +7)