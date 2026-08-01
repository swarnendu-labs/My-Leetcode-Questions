class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    ans += 4
                    if i > 0 and grid[i - 1][j]:
                        ans -= 2
                    if j > 0 and grid[i][j - 1]:
                        ans -= 2

        return ans