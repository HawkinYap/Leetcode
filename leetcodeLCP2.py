class Solution(object):
    def fraction(self, cont):
        """
        :type cont: List[int]
        :rtype: List[int]
        """
        # cont_re = cont[::-1]
        # fz = 1
        # fm = cont_re[0]
        # for i in range(1, len(cont_re)):
        #     tmp = fm
        #     fz = cont_re[i] * fm + fz
        #     fm = tmp
        #     print(fz, fm)
        #     fz, fm = fm, fz
        #     if fm == 0:
        #         return(None)
        # fz, fm = fm, fz
        # return([fz, fm])

        if len(cont) == 1:
            print('***')
            print(cont)
            return [cont[0], 1]
        elif len(cont) == 2:
            a, b = cont
            print(cont, a, b)
            return [a*b+1, b]
        else:
            b, a = self.fraction(cont[1:])
            print('---')
            print(b, a)
            return([b*cont[0]+a, b])




if __name__ == "__main__":
    cont = [3, 2, 0, 2]
    # cont = [0, 0, 3]
    s = Solution()
    print(s.fraction(cont))