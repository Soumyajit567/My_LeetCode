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
        if s[0] != '[':
            # It's just a single integer, not a list.
            return NestedInteger(int(s))
        
        stack = []
        number = ''
        for char in s:
            if char == '[':
                stack.append(NestedInteger())  # Start a new Nested List
            elif char.isdigit() or char == '-':
                number += char  # Build the number
            elif char == ',' or char == ']':
                if number:
                    # If there is a number buffered, add it to the most recent list.
                    stack[-1].add(NestedInteger(int(number)))
                    number = ''  # Reset the number buffer.
                if char == ']' and len(stack) > 1:
                    # End of this list, pop and add to the next one up.
                    ni = stack.pop()
                    stack[-1].add(ni)
        
        return stack[0]  # The first element of the stack is the deserialized NestedInteger.