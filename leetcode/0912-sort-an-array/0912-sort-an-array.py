class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)   # ✅ IMPORTANT

        def merge(left, right):
            i, j = 0, 0
            merged = []

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged

        return mergeSort(nums)   # ✅ START RECURSION