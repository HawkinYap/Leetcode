class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Bit = ""
        # for i in bin(num)[2:]:
        #     if i == '0':
        #         Bit += "1"
        #     else:
        #         Bit += "0"
        # return(int('0b' + Bit, 2))
        return(int("".join(map(lambda x: '1' if x == '0' else '0', bin(num)[2:])), 2))

if __name__ == '__main__':
    num = 5
    s = Solution()
    print(s.findComplement(num))