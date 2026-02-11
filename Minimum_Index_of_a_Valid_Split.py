class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        first_map = defaultdict(int)
        second_map = defaultdict(int)

        for num in nums:
            first_map[num] += 1

        n = len(nums)
        for idx in range(n):
            num = nums[idx]
            first_map[num] -= 1
            second_map[num] += 1

            #check validity
            if second_map[num]*2 > idx + 1 and first_map[num]*2 > n - idx -1:
                return idx

        return -1