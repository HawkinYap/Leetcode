class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        
        stack = [pRoot]
        nextLayer = []
        result = []
        flag = -1
        
        while stack:
            for i in stack:
                if i.left:
                    nextLayer.append(i.left)
                if i.right:
                    nextLayer.append(i.right)
            if flag > 0:
                stack1 = stack[::-1]
                result.append([i.val for i in stack1])
            else:
                result.append([i.val for i in stack])
            print(result)
            flag = -1 * flag
            stack, nextLayer = nextLayer, []
            
        print(result)

if __name__ == "__main__":
    a = TreeNode(5)
    b = TreeNode(3)
    c = TreeNode(7)
    a.left = b
    a.right = c

    d = TreeNode(2)
    e = TreeNode(4)
    f = TreeNode(8)

    b.left = d
    c.left = e
    c.right = f

    g = TreeNode(6)
    e.right = g


    s = Solution()
    print(s.Print(a))