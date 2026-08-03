class Solution:
    def findSubsequences(self, nums):
        res = []
        path = []

        def dfs(idx):
            if len(path) >= 2:
                res.append(path[:])
            used = set()
            for i in range(idx, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    used.add(nums[i])
                    path.append(nums[i])
                    dfs(i + 1)
                    path.pop()

        dfs(0)
        return res