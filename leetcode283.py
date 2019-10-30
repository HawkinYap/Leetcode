class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # z = []
        # n = []
        # for i in nums:
        #     if i == 0:
        #         z.append(i)
        #     else:
        #         n.append(i)
        # return(n + z)
        nums.sort(key=bool, reverse=True)
        return(nums)

if __name__ == "__main__":
    nums = [0,12,0,3,14]
    s = Solution()
    print(s.moveZeroes(nums))