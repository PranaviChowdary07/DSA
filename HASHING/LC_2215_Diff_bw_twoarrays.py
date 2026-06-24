class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1set = set(nums1)
        num2set = set(nums2)
        res1, res2 = set(), set()

        for n in num1set:
            if n not in num2set:
                res1.add(n)
        for n in num2set:
            if n not in num1set:
                res2.add(n)
        return [list(res1),list(res2)]


        