class TrieNode:
    def __init__(self):
        self.child = [None, None]


class Solution:
    def findMaximumXOR(self, nums):
        root = TrieNode()

        # Insert a number into the trie
        def insert(num):
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if node.child[bit] is None:
                    node.child[bit] = TrieNode()
                node = node.child[bit]

        # Find the maximum XOR for a number
        def query(num):
            node = root
            ans = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opposite = bit ^ 1
                if node.child[opposite]:
                    ans |= (1 << i)
                    node = node.child[opposite]
                else:
                    node = node.child[bit]
            return ans

        for num in nums:
            insert(num)

        res = 0
        for num in nums:
            res = max(res, query(num))

        return res