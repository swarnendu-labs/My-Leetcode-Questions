from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        queue = deque()

        # Add border O's
        for r in range(rows):
            if board[r][0] == "O":
                queue.append((r, 0))
            if board[r][cols - 1] == "O":
                queue.append((r, cols - 1))

        for c in range(cols):
            if board[0][c] == "O":
                queue.append((0, c))
            if board[rows - 1][c] == "O":
                queue.append((rows - 1, c))

        # Mark all O's connected to border as safe
        while queue:
            r, c = queue.popleft()

            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != "O"
            ):
                continue

            board[r][c] = "S"

            queue.append((r + 1, c))
            queue.append((r - 1, c))
            queue.append((r, c + 1))
            queue.append((r, c - 1))

        # Capture surrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"