class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        # listV = []
        # _index = 0
        # for i in pushV:
        #     if i != popV[_index]:
        #         listV.append(i)
        #     else:
        #         _index += 1
        #         while listV and listV[-1] == popV[_index]:
        #             listV.pop()
        #             _index += 1
        # if len(listV) != 0:
        #     return False
        # else:
        #     return True

        stack = []
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if not stack:
            return True
        else:
            return False


if __name__ == "__main__":
    pushV = [1,2,3,4,5]
    popV = [4,3,5,1,2]
    s = Solution()
    print(s.IsPopOrder(pushV, popV))