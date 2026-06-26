from collections import Counter
from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        values_map = Counter(arr)
        ans= -1
        for val, freq in values_map.items():
            if (val == freq and val > ans):
                ans = val
        return ans
        