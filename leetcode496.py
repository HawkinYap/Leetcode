class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        hashmap = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                hashmap[stack.pop()] = num
            stack.append(num)

        return [hashmap.get(x, -1) for x in nums1]
        
if __name__ == '__main__':
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    s = Solution()
    print(s.nextGreaterElement(nums1, nums2))
