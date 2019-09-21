class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return(nums)
        l = []
        new = []
        for i in range(len(nums)):
            l += nums[i]
        print(l)
        for i in range(0, len(l), c):
            new.append(l[i:i+c])

        return(new)

if __name__ == '__main__':
    nums = [[1,2],  [3,4]]
    r = 4
    c = 1
    s = Solution()
    print(s.matrixReshape(nums, r, c))