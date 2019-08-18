class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # res = []
        # for i in range(left, right + 1):
        #     tmp = []
        #     flag = 0
        #     k = i
        #     while k > 0 :
        #         tmp.append(k % 10)
        #         k = k//10
        #     for j in tmp:
        #         if j == 0:
        #             flag = 1
        #             continue
        #         if i % j != 0:
        #             flag = 1
        #     if flag == 0 :
        #         res.append(i)   
        # return(res)
        return [i for i in range(left,right+1) if not any([m == '0' or i % int(m) != 0 for m in str(i)])]
        

if __name__ == '__main__':
    left = 1
    right = 22
    solution = Solution()
    print(solution.selfDividingNumbers(left, right))
