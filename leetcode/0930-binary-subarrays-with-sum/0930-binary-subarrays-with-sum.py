class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict

        c = defaultdict(int)
        c[0] = 1
        prefixSum = 0
        result = 0
        for num in nums:
            prefixSum += num
            result += c[prefixSum - goal]
            c[prefixSum] += 1

        return result
        