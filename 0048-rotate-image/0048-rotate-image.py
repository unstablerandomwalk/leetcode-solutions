class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[matrix[n-1-j][i] for j in range(n)] for i in range(n)]
        for i in range(n):
            matrix[i][:] = rotated[i] 