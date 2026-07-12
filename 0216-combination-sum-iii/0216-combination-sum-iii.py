class Solution:
    def combinationSum3(self, k, n):
        res = []

        def dfs(start, rem, path):
            if len(path) == k:
                if rem == 0:
                    res.append(path[:])
                return
            for i in range(start, 10):
                if i > rem:
                    break
                path.append(i)
                dfs(i + 1, rem - i, path)
                path.pop()

        dfs(1, n, [])
        return res