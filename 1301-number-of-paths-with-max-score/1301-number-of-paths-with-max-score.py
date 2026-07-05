from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                best = -1
                count = 0

                for ni, nj in [(i + 1, j), (i, j + 1), (i + 1, j + 1)]:
                    if ni < n and nj < n and score[ni][nj] != -1:
                        if score[ni][nj] > best:
                            best = score[ni][nj]
                            count = ways[ni][nj]
                        elif score[ni][nj] == best:
                            count = (count + ways[ni][nj]) % MOD

                if best == -1:
                    continue

                value = 0 if board[i][j] == 'E' else int(board[i][j])

                score[i][j] = best + value
                ways[i][j] = count

        if score[0][0] == -1:
            return [0, 0]

        return [score[0][0], ways[0][0]]