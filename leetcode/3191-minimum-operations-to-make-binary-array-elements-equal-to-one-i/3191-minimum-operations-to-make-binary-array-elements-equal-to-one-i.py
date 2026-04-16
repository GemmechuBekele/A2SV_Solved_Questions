class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        op = 0
        for i in range(n):
            if nums[i]==0:
                if i+2 >= n:
                    return -1
                for j in range(i, i+3):
                    nums[j] ^= 1
                op += 1
        return op