class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return(sum(nums[::2]))

if __name__ == '__main__':
    nums = [1, 4, 3, 2, 5, 6]
    s = Solution()
    print(s.arrayPairSum(nums))