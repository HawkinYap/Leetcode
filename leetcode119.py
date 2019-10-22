class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # rowIndex += 1
        # res = [1] * rowIndex
        # index = 3
        # while index <= rowIndex:
        #     tmp = res.copy()
        #     for i in range(1, index - 1):
        #         res[i] = tmp[i - 1] + tmp[i]
        #     index += 1
        # return(res)

        i, result = 0, [1]
        while i < rowIndex:
            result = [1] + [result[x] + result[x + 1] for x in range(len(result) - 1)] + [1]
            i += 1
        return(result)

if __name__ == "__main__":
    rowIndex = 4
    s = Solution()
    print(s.getRow(rowIndex))