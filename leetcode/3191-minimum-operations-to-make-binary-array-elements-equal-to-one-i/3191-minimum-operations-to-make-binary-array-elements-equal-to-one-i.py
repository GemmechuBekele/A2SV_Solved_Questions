class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        diff = [0]*n
        operations = 0
        flip_effect = 0

        for i in range(n):
            flip_effect += diff[i]
            current = nums[i]^(flip_effect % 2)
            if current == 0:
                if i+2 >= n:
                    return -1
                operations += 1
                flip_effect += 1

                diff[i] += 1
                if i + 3 < n:
                    diff[i + 3] -= 1
        return operations