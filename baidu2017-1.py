import time

class Solution():
    def find(self, N, Nlist):
        for i in Nlist:
            if i < 0 or i > 1000:
                return -1
        if N == len(Nlist):
            a = set(Nlist)
            if len(a) > 2:
                b = sorted(list(a))
                return (b[2])
            else:
                return -1
        else:
            return -1

if __name__ == "__main__":
    N = input()
    Nlist = list(map(int, raw_input().split()))
    start = time.clock()
    s = Solution()
    print(s.find(N, Nlist))
    end = time.clock()
    print(start - end)
