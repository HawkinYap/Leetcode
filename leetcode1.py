class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = {}
        for i in range(len(nums)):
            j = nums[i]
            if target - j in list:
                return ([list[target-j],i])
            list[j]=i

if __name__ == "__main__" :
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))