class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # res = []
        # for i in range(1, numRows + 1):
        #     tmp = [1] * i
        #     res.append(tmp)
        
        # for i in range(2, len(res)):
        #     for j in range(1, i):
        #         res[i][j] = res[i - 1][j - 1] + res[i - 1][j]     

        # return(res)

        r = [[1]]
        for i in range(1,numRows):
            r.append(list(map(lambda x,y:x+y, [0]+r[-1],r[-1]+[0])))
        # return r[:numRows]
        return r

if __name__ == '__main__':
    numRows = 5
    s = Solution()
    print(s.generate(numRows))