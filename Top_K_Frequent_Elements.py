from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        topk = []
        for num, freq in count.most_common(k):
                topk.append(num)
        return topk