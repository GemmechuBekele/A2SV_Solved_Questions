class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_prefix = 0
        min_prefix = 0
        max_sum = float('-inf')

        for x in nums:
            current_prefix += x
            max_sum = max(max_sum, current_prefix - min_prefix)
            min_prefix = min(min_prefix, current_prefix)

        return max_sum
        