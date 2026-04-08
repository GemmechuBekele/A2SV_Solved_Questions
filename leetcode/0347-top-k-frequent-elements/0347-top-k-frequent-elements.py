class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        count = Counter(nums)
        
        buckets = [[] for _ in range(n+1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans


        