class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        maxArea = 0

        for row in matrix:
            # Build histogram
            for j in range(cols):
                if row[j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0


            stack = []
            temp = heights + [0]

            for i in range(len(temp)):
                while stack and temp[stack[-1]] > temp[i]:
                    h = temp[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    maxArea = max(maxArea, h * width)

                stack.append(i)

        return maxArea