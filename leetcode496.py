class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # res = []
        # for i in nums1:
        #     if i == max(nums2):
        #         res.append(-1)
        #     elif i == nums2[-1]:
        #         res.append(-1)
        #     else:
        #         tmp = nums2.index(i)
        #         m = nums2[tmp + 1:]
        #         flag = 0
        #         for j in m:
        #             if j > i:
        #                 flag = 1
        #                 res.append(j)
        #                 break
        #         if flag == 0:
        #             res.append(-1)
                
        # return(res)

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
