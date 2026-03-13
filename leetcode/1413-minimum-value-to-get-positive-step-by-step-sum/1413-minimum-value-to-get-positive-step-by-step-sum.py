class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        
        minPrefix = min(prefix)
        startValue = 1
        while startValue:
            if startValue + minPrefix >=1:
                return startValue
            startValue += 1
        