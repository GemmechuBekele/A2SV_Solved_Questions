class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * (n + 1) 

        # frequency
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1

        # Convert to prefix sum
        for i in range(1, n):
            freq[i] += freq[i - 1]

        freq = freq[:n]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        mod = 10**9 + 7
        ans = sum(num * f for num, f in zip(nums, freq)) % mod
        return ans
        