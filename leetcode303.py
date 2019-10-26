class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(len(self.nums)):
            if i > 0:
                self.nums[i] = self.nums[i] + self.nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return(self.nums[j] - self.nums[i-1])
        else:
            return(self.nums[j])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

if __name__ == "__main__":
    s = NumArray([-2, 0, 3, -5, 2, -1])
    print(s.sumRange(0, 2))