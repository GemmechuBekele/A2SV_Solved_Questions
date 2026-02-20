class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        flip = []
        n = len(arr)

        # I fix from largest to smallest
        for curr_size in range(n, 1, -1):

            largest = curr_size   # number I want to place

            # find index of this largest number
            for i in range(curr_size):
                if arr[i] == largest:
                    max_index = i
                    break

            # if already in correct position, skip
            if max_index == curr_size - 1:
                continue

            # bring largest to front (if not already there)
            if max_index != 0:
                flip.append(max_index + 1)
                arr[:max_index+1] = reversed(arr[:max_index+1])

            # move largest to correct position
            flip.append(curr_size)
            arr[:curr_size] = reversed(arr[:curr_size])

        return flip