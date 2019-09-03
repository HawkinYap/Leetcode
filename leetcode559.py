# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return(0)
        if not root.children:
            return(1)
        return(1 + max(self.maxDepth(child) for child in root.children))

if __name__ == '__main__':
    n5 = Node(5,None)
    n6 = Node(6,None)
    n3 = Node(2,None)
    n4 = Node(4,None)
    n2 = Node(3,[n5,n6])
    n1 = Node(1,[n2,n3,n4])

    s = Solution()
    print(s.maxDepth(n1))

    