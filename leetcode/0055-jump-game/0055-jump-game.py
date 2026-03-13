class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        n = len(nums)
        for i in range(n):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])
            if maxJump >= n-1:
                return True
        