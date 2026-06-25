# Find the majority element
    # In this problem states only find majority element and this problems only exists one majority element because condition is  n//2

from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            if num in freq:
                freq[num]+1
            else:
                freq[num]= 1
            if freq[num]>len(nums)//2:
                return num
#Optimal Solution (Boyer-Moore)
class Solution:
    def majorityElement(self, nums):
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
# Find the majority elements more than 1 condition is n//3
class Solution:
    def majorityElement(self, nums):
        freq = {}
        for num in nums:

            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        res = []
        for num in freq:
            if freq[num] > len(nums) // 3:
                res.append(num)
        return res