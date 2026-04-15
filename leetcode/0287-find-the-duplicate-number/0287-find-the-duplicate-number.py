class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = self.cycle_sort(nums)
        m = len(arr)
        for i in range(m):
            if arr[i] != i+1:
                return arr[i]

    def cycle_sort(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i] - 1
            if nums[i] != nums[pos]:
                nums[i], nums[pos] = nums[pos], nums[i]
            else: 
                i += 1
        return nums
