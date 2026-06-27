class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row needs to be zeroed
        for j in range(cols):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column needs to be zeroed
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and first column as markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero rows based on markers
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0

        # Zero columns based on markers
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(1, rows):
                    matrix[i][j] = 0

        # Zero first row if needed
        if first_row_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Zero first column if needed
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0