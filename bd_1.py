class Solution(object):
    def d(num, target):
        return num > target

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))