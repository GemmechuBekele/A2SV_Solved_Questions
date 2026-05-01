class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Edge case
        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        # If all elements are the same
        if min_val == max_val:
            return 0

        # Bucket size and count
        bucket_size = math.ceil((max_val - min_val) / (n - 1))
        bucket_count = (max_val - min_val) // bucket_size + 1

        # Initialize buckets
        bucket_min = [float('inf')] * bucket_count
        bucket_max = [float('-inf')] * bucket_count

        # Place numbers into buckets
        for num in nums:
            idx = (num - min_val) // bucket_size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)

        # Find maximum gap
        max_gap = 0
        prev_max = min_val

        for i in range(bucket_count):
            if bucket_min[i] == float('inf'):
                continue  # empty bucket
            max_gap = max(max_gap, bucket_min[i] - prev_max)
            prev_max = bucket_max[i]

        return max_gap
        