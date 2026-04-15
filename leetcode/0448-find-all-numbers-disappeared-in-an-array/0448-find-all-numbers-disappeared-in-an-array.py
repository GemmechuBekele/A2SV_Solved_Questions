class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = self.cycle_sort(nums)
        res = []
        n = len(arr)
        for i in range(n):
            if arr[i] != i+1:
                res.append(i+1)
        return res

    def cycle_sort(self, nums):
        i = 0
        n = len(nums)
        while i < n:
            pos = nums[i] - 1
            if nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        return nums
        