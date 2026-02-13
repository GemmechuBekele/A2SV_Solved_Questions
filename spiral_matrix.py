class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        #Determine direction point
        top = 0
        left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1

        # empty list store all element
        spiral_list = []

        while top <= bottom and left <= right:
            #move from left to right(top row)
            for i in range(left, right+1):
                spiral_list.append(matrix[top][i])
            top +=1

             #move from top to bottom (right column)
            for i in range(top, bottom+1):
                spiral_list.append(matrix[i][right])

            right -= 1

            #move from right to left (bottom column)
            if top <= bottom:
                for i in range(right, left-1, -1):
                    spiral_list.append(matrix[bottom][i])

                bottom -= 1

            # bottom to top
            if left <= right:
                for i in range(bottom, top-1, -1):
                    spiral_list.append(matrix[i][left])

                left += 1

        return spiral_list