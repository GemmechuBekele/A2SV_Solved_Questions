class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        n = len(mat)
        for _ in range(4): 
            if mat == target:
                return True
                
            new_mat = [[0]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    new_mat[i][j] = mat[n-j-1][i]

            mat = new_mat

        return False
