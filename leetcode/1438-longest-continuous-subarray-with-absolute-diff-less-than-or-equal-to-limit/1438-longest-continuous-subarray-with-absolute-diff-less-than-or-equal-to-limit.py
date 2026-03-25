class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        maxDeque = deque()
        minDeque = deque()
        ans = 0
        for right in range(len(nums)):
            num = nums[right]
            while maxDeque and num > maxDeque[-1]:
                maxDeque.pop()

            maxDeque.append(num)

            while minDeque and num < minDeque[-1]:
                minDeque.pop()

            minDeque.append(num)

            while maxDeque[0] - minDeque[0] > limit:
                if nums[left] == maxDeque[0]:
                    maxDeque.popleft()

                if nums[left] == minDeque[0]:
                    minDeque.popleft()

                left += 1
            ans = max(ans, right - left + 1)
        return ans
        