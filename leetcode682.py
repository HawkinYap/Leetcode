class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # res = []
        # num = 0
        # for op in ops:
        #     if op == 'C':
        #         res.pop()
        #         num -= res[-1]
        #     elif op == 'D':
        #         tmp = res[-1] * 2
        #         num += tmp
        #         res.append(tmp)
        #     elif op == '+':
        #         tmp = res[-2] + res[-1]
        #         num += tmp
        #         res.append(tmp)
        #     else:
        #         res.append(int(op))
        #         num += int(op)
        #     return(sum(res))

        stack = []
        for op in ops:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)
            

if __name__ == '__main__':
    ops = ["5","-2","4","C","D","9","+","+"]
    s = Solution()
    print(s.calPoints(ops))