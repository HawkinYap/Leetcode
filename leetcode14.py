class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        #minl = min([len(x) for x in strs])
        minl = 1000
        for x in strs:
            if len(x) < minl:
                minl = len(x)
        end = 0
        while end < minl:
            for i in range(1,len(strs)):
                if strs[i][end]!= strs[i-1][end]:
                    return strs[0][:end]
            end += 1
        return strs[0][:end]
if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(strs))