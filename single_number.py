from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)

        for i, j in enumerate(nums):
            if count[j] == 1:
                return nums[i]