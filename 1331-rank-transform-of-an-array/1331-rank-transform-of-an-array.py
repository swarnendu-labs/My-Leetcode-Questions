class Solution:
    def arrayRankTransform(self, arr):
        rank = {}
        for i, v in enumerate(sorted(set(arr)), 1):
            rank[v] = i
        return [rank[x] for x in arr]