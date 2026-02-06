class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_index = {}
        for index1, value in enumerate(list1) :
            common_index[value] = index1

        minSum = float("inf")
        common_string = []

        for index2, value in enumerate(list2):
            if value in common_index:
                sum_two = common_index[value] + index2

                if sum_two < minSum:
                    minSum = sum_two
                    common_string = [value]
                elif sum_two == minSum:
                    common_string.append(value)
        
        return common_string
                