class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return(list(set(nums1) & set(nums2)))
        
if __name__ == '__main__':
    nums1, nums2 = [4,9,5], [9,4,9,8,4]
    s = Solution()
    print(s.intersection(nums1, nums2))