import math
class Solution():
    def find(self, N, Nlist):
        for i in Nlist:
            if  abs(i) > 100:
                return -1
        if N == len(Nlist):
            a = [abs(i) for i in Nlist]
            amax = max(a)
            Nlist.remove(amax)
            sum = 0
            for i in Nlist:
                sum += i            
            print(sum)
            
        else:
            return -1



if __name__ == "__main__":
    N = input()
    Nlist = list(map(int, raw_input().split()))
    s = Solution()
    print(s.find(N, Nlist))
