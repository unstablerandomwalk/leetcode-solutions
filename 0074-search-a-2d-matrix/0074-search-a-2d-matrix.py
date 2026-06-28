class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False