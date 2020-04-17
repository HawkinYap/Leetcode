class Solution:
    def maxInWindows(self, num, size):
        # write code here
        # if not size or not num:
        #     return []

        # maxlst = []
        # for i in range(0, len(num) - size + 1):
        #     maxlst.append(max(num[i:i+size]))

        # return maxlst
        queue,res,i = [],[],0
        while size>0 and i<len(num):
            if len(queue)>0 and i-size+1 > queue[0]: #若最大值queue[0]位置过期 则弹出
                queue.pop(0)
            while len(queue)>0 and num[queue[-1]]<num[i]: #每次弹出所有比num[i]的数字
                queue.pop()
            queue.append(i)
            print(queue)
            if i>=size-1:
                res.append(num[queue[0]])
            i += 1
        return res




if __name__ == "__main__":
    num = [4,3,5,6,2,7]
    size = 3
    s = Solution()
    print(s.maxInWindows(num, size))