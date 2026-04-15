class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = self.cycle_sort(nums)
        m = len(arr)
        for i in range(m):
            if i != arr[i]:
                return i
        return m
       
    # nums.sort()
    def cycle_sort(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            pos = nums[i]
            if nums[i] < n and nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        return nums
        
        
        