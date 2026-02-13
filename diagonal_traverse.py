class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        diagonal_arr = []
        rows = len(mat)
        cols = len(mat[0])

        # total number of diagonal, t = rows + cols -1
        # every diagonal is i + j, d = i + j
        t = rows + cols -1

        for d in range(t):
            # store temporary list before eveness or oddness is checked
            temp = []
            
            for i in range(rows):
                j = d -i # d = i + j

                #To Make sure column is valid.
                if 0 <=j < cols:
                    temp.append(mat[i][j])

            if d % 2 == 0: # if d is even reverse it.
                diagonal_arr.extend(temp[::-1]) # reverse

            else:# if d is odd put as normal.
                diagonal_arr.extend(temp)

        return diagonal_arr