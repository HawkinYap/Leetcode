# Definition for a Node.
class Node:
    def __init__(self, val,children):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root):
        if(root == None):
            return
        else:
            self.res.append(root.val)
            if(root.children):
                for child in root.children:
                    self.preorder(child)
            return(self.res)

n5 = Node(5,None)
n6 = Node(6,None)
n3 = Node(2,None)
n4 = Node(4,None)

n2 = Node(3,[n5,n6])
n1 = Node(1,[n2,n3,n4])

s = Solution()
result = s.preorder(n1)
print(result)
