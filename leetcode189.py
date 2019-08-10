
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        nums[:] = nums[nums_len - k:] + nums[: nums_len - k]
        
        print (nums)
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)