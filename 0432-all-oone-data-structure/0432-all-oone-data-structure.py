class Node:
    def __init__(self, cnt):
        self.cnt = cnt
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.mp = {}

    def _insert_after(self, node, new_node):
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.mp:
            if self.head.next != self.tail and self.head.next.cnt == 1:
                node = self.head.next
            else:
                node = Node(1)
                self._insert_after(self.head, node)
            node.keys.add(key)
            self.mp[key] = node
            return

        node = self.mp[key]
        nxt = node.next
        if nxt != self.tail and nxt.cnt == node.cnt + 1:
            new_node = nxt
        else:
            new_node = Node(node.cnt + 1)
            self._insert_after(node, new_node)

        new_node.keys.add(key)
        self.mp[key] = new_node

        node.keys.remove(key)
        if not node.keys:
            self._remove(node)

    def dec(self, key: str) -> None:
        node = self.mp[key]

        if node.cnt == 1:
            del self.mp[key]
        else:
            prv = node.prev
            if prv != self.head and prv.cnt == node.cnt - 1:
                new_node = prv
            else:
                new_node = Node(node.cnt - 1)
                self._insert_after(prv, new_node)

            new_node.keys.add(key)
            self.mp[key] = new_node

        node.keys.remove(key)
        if not node.keys:
            self._remove(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()