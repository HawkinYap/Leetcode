class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        newBit = ""
        for i in bin(num)[2:]:
            if i == '0':
                newBit += "1"
            else:
                newBit += "0"
        return(int('0b' + newBit, 2))

if __name__ == '__main__':
    num = 5
    s = Solution()
    print(s.findComplement(num))