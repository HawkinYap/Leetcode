class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        tmp = 0
        
        for num in A:
            if num % 2 == 0:
                tmp += num
                
        for val, ind in queries:
            pre = A[ind]
            if pre % 2 == 0:
                tmp -= pre
            A[ind] = pre + val
            if A[ind] % 2 == 0:
                tmp += A[ind]
            res.append(tmp)
            
        return res

if __name__ == "__main__":
    A = [1,2,3,4]
    queries = [[1,0],[-3,1],[-4,0],[2,3]]
    s = Solution()
    print(s.sumEvenAfterQueries(A, queries))