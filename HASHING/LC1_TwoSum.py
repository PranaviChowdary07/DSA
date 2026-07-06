class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
#nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
#target = int(input("Enter target: "))
nums = [2,3,4,5,6]
target = 7
obj = Solution()
print(obj.twoSum(nums, target))