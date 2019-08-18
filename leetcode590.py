# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return([])
        if not root.children:
            return([root.val])
        result = []
        for child in root.children:
            result += self.postorder(child)
        result += [root.val]
        return(result)

    
n5 = Node(5,None)
n6 = Node(6,None)
n3 = Node(2,None)
n4 = Node(4,None)
n2 = Node(3,[n5,n6])
n1 = Node(1,[n2,n3,n4])

s = Solution()
result = s.postorder(n1)
print(result)
