# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return([])                                 

        cur_layer = [root]                            
        res = []                                        
        while cur_layer:                         
            res.append(sum(node.val for node in cur_layer) / len(cur_layer))
            next_layer = []                             
            for node in cur_layer:
                if node.left:                     
                    next_layer.append(node.left)      
                if node.right:                 
                    next_layer.append(node.right) 
            cur_layer = next_layer                

        return(res)   
        
        

if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(15)
    n5 = TreeNode(7)
    n3.left = n4
    n3.right = n5
    s = Solution()
    print(s.averageOfLevels(n1))