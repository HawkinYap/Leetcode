class Solution(object):
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        z = 0
        indx = 0
        for ele in s:
            if indx < len(g) and ele >= g[indx] :
                z += 1
                indx +=1 
        return z 