class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        le = 0
        n = len(people)
        ri = n-1
        count = 0
        while le <= ri:
            weight = people[le]+people[ri]
            if weight <= limit:
                count += 1
                le += 1
                ri -= 1
            else:
                count += 1
                ri -= 1
        return count
        