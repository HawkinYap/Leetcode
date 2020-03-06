class Solution:
    def Find(self, target, array):
        for row in array:
            if target in row:
                return True
        return False




if __name__ == "__main__":
    a = [[1,2,3,4],[6,7,8,9],[11,12,13,14]]
    num = 5
    s = Solution()
    print(s.Find(num, a))
    