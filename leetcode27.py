class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # print(nums)
        # return(len(nums))

        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    s = Solution()
    print(s.removeElement(nums, val))