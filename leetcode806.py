class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line, count = 0, 0
        line_count = 0
        for i in S:
            l = widths[ord(i) - ord('a')]
            line_count += l
            print(widths[ord(i) - ord('a')])
            if line_count == 100:
                line_count = 0
                count +=1
            if line_count > 100:
                print(line_count)
                line_count = l
                count += 1          
        return([count + 1, line_count])




if __name__ == '__main__':
    # widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    # S = "abcdefghijklmnopqrstuvwxyz"
    widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "bbbcccdddaaa"
    s = Solution()
    print(s.numberOfLines(widths, S))
