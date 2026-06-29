from typing import List
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set(nums)
        maximum = 0
        for num in s:
            if -num in s:
                maximum = max(maximum, num)
        if maximum == 0:
            return -1
        else:
            return maximum

#case 1
#Input
#nums =[-10,8,6,7,-2,-3]
#Output
-1
#Expected
-1

#case 2
#Input
#nums =[-1,10,6,7,-7,1]
#Output
#7
#Expected
#7