class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num = set(nums)
        # if len(num) != (len(nums) + 1) / 2:
        #     return
        # for i in num:
        #     if nums.count(i) == 1:
        #         return(i)
        res = 0
        for i in nums:
            res^=i
        return res

if __name__ == '__main__':
    nums = [4,1,2,1,2]
    s = Solution()
    print(s.singleNumber(nums))