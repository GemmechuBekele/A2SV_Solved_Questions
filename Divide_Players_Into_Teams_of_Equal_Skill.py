class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        teams = int(n/2)
        total = sum(skill)

        if total % teams != 0:
            return -1

        s = int(total/teams)
        skill.sort()
        left = 0
        right = n-1
        chemistry = 0
        
        while left < right:
            pair_sum = skill[left] + skill[right]
            if  pair_sum == s:
                chemistry += (skill[left] * skill[right])
                left += 1
                right -= 1
            else:
                return -1
        return chemistry
