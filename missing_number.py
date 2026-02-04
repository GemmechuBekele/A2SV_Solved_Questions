class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for miss_num in range(n+1):
            if miss_num not in nums:
                return miss_num