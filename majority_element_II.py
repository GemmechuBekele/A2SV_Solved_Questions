class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        more = []
        for i, value in count.items():
            if value > len(nums)//3:
                more.append(i)
        return more