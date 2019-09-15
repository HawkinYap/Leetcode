# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return([])
        que = []
        res = []
        que.append(root)
        while len(que):
            l = len(que)
            sub = []
            for i in range(l):
                current = que.pop(0)
                print(current.val)
                sub.append(current.val)
                if current.children:
                    for child in current.children:
                        que.append(child)
            res.append(sub)
        return(res)


if __name__ == '__main__':
    n3 = Node(2, None)
    n4 = Node(4, None) 

    n5 = Node(5, None)
    n6 = Node(6, None)
    n2 = Node(3, [n5, n6])
    n1 = Node(1, [n2, n3, n4])

    s = Solution()
    print(s.levelOrder(n1))