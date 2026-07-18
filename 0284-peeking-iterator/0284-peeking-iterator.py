# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def hasNext(self) -> bool:
#     def next(self) -> int:

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.nxt = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self.nxt

    def next(self):
        val = self.nxt
        self.nxt = self.iterator.next() if self.iterator.hasNext() else None
        return val

    def hasNext(self):
        return self.nxt is not None