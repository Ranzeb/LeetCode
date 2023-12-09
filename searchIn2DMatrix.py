#https://leetcode.com/problems/search-a-2d-matrix/

class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = m*n - 1

        while(low <= high): 
            mid = (high + low) // 2
            row = mid // 2
            col = mid % 2

            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] < target):
                low = mid + 1
            else:
                high = mid - 1
        return False