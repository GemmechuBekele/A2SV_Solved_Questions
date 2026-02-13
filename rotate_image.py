class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        #New matrix
        new_matrix = [[0]*row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                new_matrix[j][row-1-i] = matrix[i][j]

        result = new_matrix

        for i in range(row-1, -1, -1):
            for j in range(col-1, -1, -1):
                matrix[i][j] = result[i][j]