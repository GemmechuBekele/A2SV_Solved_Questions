class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        arr = self.cycle_sort(nums)
        m = len(arr)
        for i in range(m):
            if nums[i] != i+1:
                return i+1
        return m+1
    def cycle_sort(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if 1 <= nums[i] and nums[i] <= n:
                pos = nums[i] - 1
                if nums[i] != nums[pos]:
                    nums[i], nums[pos] = nums[pos], nums[i]
                else: i += 1
            else: i += 1
        return nums
        