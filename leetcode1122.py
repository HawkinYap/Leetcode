class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        # f = []
        # for a in arr2:
        #     f.append([a] * arr1.count(a))

        # newList = []
        # for item in f:
        #     if type(item) == list:
        #         for i in item:
        #             newList.append(i)
        #     else:
        #         newList.append(item)

        # c = sorted([x for x in arr1 if x not in arr2])
        # return(newList + c)

        order = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1 , key=lambda a: order.get(a, 1000 + a))


        
if __name__ == '__main__':
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]

    s = Solution()
    print(s.relativeSortArray(arr1, arr2))