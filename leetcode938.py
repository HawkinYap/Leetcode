class Tree(object):
    def __init__(self):
        self.root = None

class Node(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
    
def TreeInsert(T, z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.val < x.val:
            x = x.left
        else:
            x = x.right
    z.parent = y
    if y == None:
        T.root = z
    elif z.val < y.val:
        y.left = z
    else:
        y.right = z
    z.left = None
    z.right = None
    return(z.val)

def Transplant(T, u, v):
    if u.parent == None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v
    if v != None:
        v.parent = u.parent

def TreeMin(x):
    while x.left != None:
        x = x.left
    return(x)

def TreeDelete(T, z):
    if z.left == None:
        Transplant(T, z, z.right)
    elif z.right==None:
        Transplant(T,z,z.left)
    else:
        y=TreeMin(z.right)
        if y.parent!=z:
            Transplant(T,y,y.right)
            y.right=z.right
            y.right.parent=y
        Transplant(T,z,y)
        y.left=z.left
        y.left.parent=y
    return(z.key)

def Midsort(root):
    if root!= None:
        Midsort(root.left)
        if root.key!=0:
            print(root.key)
        Midsort(root.right)

def Behsort(root):
    if root!= None:
        Behsort(root.left)
        Behsort(root.right)
        if root.key != 0:
            print(root.key)

def Presort(root):
    if root!= None:
        if root.key != 0:
            print(root.key)
        Presort(root.left)
        Presort(root.right)


class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        if not root:
            return 0
        if L <= root.val <= R:
            res += root.val
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
        return res

    
    
if __name__ == '__main__':
    node = [10, 5, 15, 3, 7, 0, 18]
    T = Tree()
    for nodes in node:
        print(TreeInsert(T, Node(nodes)))

    solution = Solution()
    print(solution.rangeSumBST(T.root, 7, 15))


            



    

