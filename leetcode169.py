class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count, maj = 1, nums[0]
        # for i in range(1, len(nums)):
        #     if maj == nums[i]:
        #         count += 1
        #     else:
        #         count -= 1
        #         if count == 0:
        #             maj = nums[i + 1]
        # return(maj)
        # nums.sort()
        # return nums[int(len(nums)/2)]
        return(max(set(nums), key=nums.count))

if __name__ == '__main__':
    nums = [3, 2, 3]
    s = Solution()
    print(s.majorityElement(nums))