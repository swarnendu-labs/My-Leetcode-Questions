from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])

        def bfs(starts):
            vis = [[False] * n for _ in range(m)]
            q = deque(starts)
            for x, y in starts:
                vis[x][y] = True
            while q:
                x, y = q.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny] and heights[nx][ny] >= heights[x][y]:
                        vis[nx][ny] = True
                        q.append((nx, ny))
            return vis

        pacific = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        atlantic = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        p = bfs(pacific)
        a = bfs(atlantic)

        return [[i, j] for i in range(m) for j in range(n) if p[i][j] and a[i][j]]