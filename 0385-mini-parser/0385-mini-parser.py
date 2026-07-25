# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()
        
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        num = None
        sign = 1
        
        for i, char in enumerate(s):
            if char == '-':
                sign = -1
            elif char.isdigit():
                if num is None:
                    num = 0
                num = num * 10 + int(char)
            elif char == '[':
                stack.append(NestedInteger())
            elif char in (',', ']'):
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    num = None
                    sign = 1
                if char == ']' and len(stack) > 1:
                    ni = stack.pop()
                    stack[-1].add(ni)
                    
        return stack[0]
        