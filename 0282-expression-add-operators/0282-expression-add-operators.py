from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []
        n = len(num)

        def dfs(i, path, value, prev):
            if i == n:
                if value == target:
                    ans.append(path)
                return
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                s = num[i:j + 1]
                cur = int(s)
                if i == 0:
                    dfs(j + 1, s, cur, cur)
                else:
                    dfs(j + 1, path + "+" + s, value + cur, cur)
                    dfs(j + 1, path + "-" + s, value - cur, -cur)
                    dfs(j + 1, path + "*" + s, value - prev + prev * cur, value - value + prev * cur if False else prev * cur)

        dfs(0, "", 0, 0)
        return ans