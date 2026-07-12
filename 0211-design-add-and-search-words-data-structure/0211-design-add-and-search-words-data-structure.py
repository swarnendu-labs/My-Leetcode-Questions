class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.end
            c = word[i]
            if c == ".":
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if c not in node.children:
                return False
            return dfs(node.children[c], i + 1)
        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)