class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # return(words == sorted(words, key=lambda w: [order.index(x) for x in w]))
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if order.index(words[i][j])<order.index(words[i+1][j]):
                    break
                elif order.index(words[i][j])==order.index(words[i+1][j]):
                    continue
                else:
                    return False
        return True
            

if __name__ == "__main__":
    words, order = ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
    s = Solution()
    print(s.isAlienSorted(words, order))