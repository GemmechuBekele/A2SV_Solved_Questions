class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            numtostr = str(i)
            for j in numtostr:
                strtonum = int(j)
                answer.append(strtonum)
            
        return answer