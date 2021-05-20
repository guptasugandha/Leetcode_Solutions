class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res, count  = 0,  [0] * 60
        for t in range(len(time)):
            index = time[t] % 60
            res += count[(60 - index)%60]
            count[index] += 1
        return res
    
    
    
    # array index res count 
    # 30      30  0     1 
    # 20      20  0     1 
    # 150     30  1     2       
    # 100     40  1     1
    # 40      40  2     2
    # 60      0   2     1
    # 60      0   3     2