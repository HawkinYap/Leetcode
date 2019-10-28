class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res=0
        for i in range(1,N+1):
            s=str(i)
            if '3' in s or '4' in s or  '7'  in s :continue            
            if '2' in s or '5' in s or '6' in s or '9' in s:res+=1
        return(res)
        # 每位都在(2, 5, 6, 9, 0, 1, 8)内，至少一位在(2, 5, 6, 9)内
        # return(len([i for i in range(1, N + 1) if not any([d for d in str(i) if int(d) in (3, 4, 7)]) and any([d for d in str(i) if int(d) in (2, 5, 6, 9)])]))


if __name__ == "__main__":
    N = 857
    s = Solution()
    print(s.rotatedDigits(N))