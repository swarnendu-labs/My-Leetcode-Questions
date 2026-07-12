class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board, words):
        root = TrieNode()
        for word in words:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = word

        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            c = board[i][j]
            if c not in node.children:
                return
            nxt = node.children[c]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None
            board[i][j] = "#"
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(ni, nj, nxt)
            board[i][j] = c
            if not nxt.children:
                del node.children[c]

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res