from collections import defaultdict
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1
        occur = list(counts.values())
        return len(occur) == len(set(occur))
arr = [1,2,3,4,1,2,3,1,1,2,2,2]
solution = Solution()
occur = solution.uniqueOccurrences(arr)
print(occur)
