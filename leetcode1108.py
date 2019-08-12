class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = address.replace('.', '[.]')
        return(res)

if __name__ == '__main__':
    address = '255.100.50.0'
    solution = Solution()
    print(solution.defangIPaddr(address))