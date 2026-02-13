class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        zero_row_set = set()
        zero_col_set = set()

        for m in range(row):
            for n in range(col):
                if matrix[m][n] == 0:
                    zero_row_set.add(m)
                    zero_col_set.add(n)

        for m in range(row):
            for n in range(col):
                if m in zero_row_set or n in zero_col_set:
                    matrix[m][n] = 0