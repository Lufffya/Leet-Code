# https://leetcode.cn/problems/spiral-matrix-ii/

from typing import List
import math


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        nums = [i + 1 for i in range(n ** 2)]
        
        nums_i = 0

        upper_row_i = 0
        upper_row_j = 0

        right_col_i = n-1
        right_col_j = 0

        Below_row_i = n-1
        Below_row_j = 0

        left_col_i = 0
        left_col_j = 0
        
        while True:
            if len(list(range(upper_row_j, n - 1 - upper_row_j))) == 0:
                if matrix[math.ceil(n / 2) - 1][math.ceil(n / 2) - 1] == 0:
                    matrix[math.ceil(n / 2) - 1][math.ceil(n / 2) - 1] = nums[-1]
                return matrix

            for i in range(upper_row_j, n - 1 - upper_row_j):
                matrix[upper_row_i][i] = nums[nums_i]
                nums_i += 1
            upper_row_i += 1
            upper_row_j += 1

            for i in range(right_col_j, n - 1 - right_col_j): 
                matrix[i][right_col_i] = nums[nums_i]
                nums_i += 1
            right_col_i -= 1
            right_col_j += 1

            for i in range(n - 1 - Below_row_j, Below_row_j, -1): 
                matrix[Below_row_i][i] = nums[nums_i]
                nums_i += 1
            Below_row_i -= 1
            Below_row_j += 1

            for i in range(n - 1 - left_col_j, left_col_j, -1): 
                matrix[i][left_col_i] = nums[nums_i]
                nums_i += 1
            left_col_i += 1
            left_col_j += 1


if __name__ == "__main__":
    n = 2
    print(Solution().generateMatrix(n))