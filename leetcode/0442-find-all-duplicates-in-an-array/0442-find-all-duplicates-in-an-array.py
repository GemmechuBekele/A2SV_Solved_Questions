class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        arr = self.quick_sort(nums)
        ans = Counter(arr)
        res = []
        for val, freq in ans.items():
            if freq == 2:
                res.append(val)
        return res
        
    def quick_sort(self, nums):
        i = 0
        n = len(nums)
        while i < n:
            pos = nums[i] - 1
            if nums[pos] != nums[i]:
                nums[pos], nums[i] = nums[i], nums[pos]
            else:
                i += 1
        return nums

        