class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        # b = str(bin(N))[2:]
        # lst = []
        # dis = []
        # for index, var in enumerate(b):
        #     if not dis and var == '1':
        #         lst.append(index)
        #         dis.append(0)
        #         continue
        #     if dis and var == '1':
        #         tmp = index - lst[-1]
        #         dis.append(tmp)
        #         lst.append(index)
        # return(max(dis))

        # tmp=bin(N)[2:]
        # start=0
        # end=0
        # res=0
        # first=True
        # for i in range(len((tmp))):
            
        #     if tmp[i]=='1' and first==True:
        #         start=i
        #         first=False
        #     elif tmp[i]=='1' and first==False:
        #         end=i
        #         res=max(res,end-start)
        #         start=i
                
        # return(res)

        ans = 0
        pre = 233
        i = 0
        while N:
            if N & 1:
                ans = max(i - pre, ans)
                pre = i
            N >>= 1
            i += 1
        return(ans)


if __name__ == "__main__":
    N = 5
    s = Solution()
    print(s.binaryGap(N))