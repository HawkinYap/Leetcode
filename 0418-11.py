class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        # if not pRoot:
        #     return True
        
        # stack = [(pRoot.left, pRoot.right)]
        
        # while stack:
        #     for i in stack:
        #         if i.left:
        #             nextlayer.append(i.left)
        #         if i.right:
        #             nextlayer.append(i.right)
        #     a = [i.val for i in stack]
        #     b = [i.val for i in stack[::-1]]
        #     if a != b:
        #         return False
        #     stack, nextlayer = nextlayer, []
        # return True
        # while stack:
        #     l, r = stack.pop()
        #     if l == None and r == None:
        #         continue
        #     if l == None or r == None:
        #         return False
        #     if l.val != r.val:
        #         return False
        #     stack.append((l.left, r.right))
        #     stack.append((l.right, r.left))
        # return True
        if pRoot == None:
            return True
        left = pRoot.left
        right = pRoot.right
        return self.isSymmetricalHelper(left, right)
    
    def isSymmetricalHelper(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val == right.val and self.isSymmetricalHelper(left.left, right.right) and self.isSymmetricalHelper(left.right, right.left):
            return True
        return False

if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(3)
    a.left = b
    a.right = c

    d = TreeNode(2)
    e = TreeNode(2)
    f = TreeNode(2)

    b.left = d
    c.left = e
    c.right = f

    g = TreeNode(2)
    b.right = g


    s = Solution()
    print(s.isSymmetrical(a))