from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        ans = [0] * 10

        ans[0] = cnt['z']
        ans[2] = cnt['w']
        ans[4] = cnt['u']
        ans[6] = cnt['x']
        ans[8] = cnt['g']

        ans[3] = cnt['h'] - ans[8]
        ans[5] = cnt['f'] - ans[4]
        ans[7] = cnt['s'] - ans[6]
        ans[1] = cnt['o'] - ans[0] - ans[2] - ans[4]
        ans[9] = cnt['i'] - ans[5] - ans[6] - ans[8]

        return ''.join(str(i) * ans[i] for i in range(10))